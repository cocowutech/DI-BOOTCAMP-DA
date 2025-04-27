from db_config import get_conn
from utils import safe_date
import pandas as pd

conn = get_conn()
cur = conn.cursor()

# students
df_students = pd.read_csv('Hackathon1/data/students.csv')
for _, row in df_students.iterrows():
    cur.execute("INSERT INTO students (student_name, dropout) VALUES (%s, %s) ON CONFLICT DO NOTHING;", (row['student_name'], row['dropout']))
conn.commit()

# courses
df_courses = pd.read_csv('Hackathon1/data/courses.csv')
for _, row in df_courses.iterrows():
    cur.execute("INSERT INTO courses (course_name) VALUES (%s) ON CONFLICT DO NOTHING;", (row['course_name'],))
conn.commit()

# sales
df_sales = pd.read_csv('Hackathon1/data/sales.csv')
for _, row in df_sales.iterrows():
    cur.execute("INSERT INTO sales (sales_name, channel_type) VALUES (%s, %s) ON CONFLICT DO NOTHING;", (row['sales_name'], row['channel_type']))
conn.commit()

# tas
df_tas = pd.read_csv('Hackathon1/data/tas.csv')
for _, row in df_tas.iterrows():
    cur.execute("INSERT INTO tas (ta_name) VALUES (%s) ON CONFLICT DO NOTHING;", (row['ta_name'],))
conn.commit()

# enrollments
df_enroll = pd.read_csv('Hackathon1/data/enrollments.csv')
for _, row in df_enroll.iterrows():
    cur.execute("SELECT student_id FROM students WHERE student_name=%s;", (row['student_name'],))
    student_id = cur.fetchone()[0]
    cur.execute("SELECT course_id FROM courses WHERE course_name=%s;", (row['course_name'],))
    course_id = cur.fetchone()[0]
    cur.execute("SELECT sales_id FROM sales WHERE sales_name=%s;", (row['sales_name'],))
    sales_id = cur.fetchone()[0]
    cur.execute("""
        INSERT INTO enrollments (student_id, course_id, sales_id, gross_income, book_cost, net_expense, net_profit, status, enrolled_date, expected_finish_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            student_id, course_id, sales_id,
            row['gross_income'], row['book_cost'],
            row['net_expense'], row['net_profit'],
            row['status'],
            safe_date(row['enrolled_date']),
            safe_date(row['expected_finish_date'])
        ))
conn.commit()

# enrollment_tas
df_etas = pd.read_csv('Hackathon1/data/enrollment_tas.csv')
for _, row in df_etas.iterrows():
    cur.execute("""
        SELECT e.enrollment_id
        FROM enrollments e
        JOIN students s ON e.student_id=s.student_id
        JOIN courses c ON e.course_id=c.course_id
        JOIN sales sa ON e.sales_id=sa.sales_id
        WHERE s.student_name=%s AND c.course_name=%s AND sa.sales_name=%s;
        """, (row['student_name'], row['course_name'], row['sales_name']))
    enrollment_id = cur.fetchone()[0]
    cur.execute("SELECT ta_id FROM tas WHERE ta_name=%s;", (row['ta_name'],))
    ta_id = cur.fetchone()[0]
    cur.execute("INSERT INTO enrollment_tas (enrollment_id, ta_id, ta_fee) VALUES (%s, %s, %s);", (enrollment_id, ta_id, row['ta_fee']))
conn.commit()

cur.close()
conn.close()
print("All data imported successfully!")
