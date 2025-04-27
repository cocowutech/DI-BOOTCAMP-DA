from db_config import get_conn
from utils import safe_date

def get_all_enrollments():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    SELECT e.enrollment_id, s.student_name, c.course_name, sa.sales_name, e.gross_income, e.status, e.enrolled_date, e.expected_finish_date
    FROM enrollments e
    JOIN students s ON e.student_id=s.student_id
    JOIN courses c ON e.course_id=c.course_id
    JOIN sales sa ON e.sales_id=sa.sales_id
    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def add_student(student_name, dropout=False):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (student_name, dropout) VALUES (%s, %s) ON CONFLICT DO NOTHING;", (student_name, dropout))
    conn.commit()
    cur.close()
    conn.close()

def delete_enrollment(enrollment_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM enrollments WHERE enrollment_id=%s;", (enrollment_id,))
    conn.commit()
    cur.close()
    conn.close()

def update_finish_date(enrollment_id, new_date):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE enrollments SET expected_finish_date=%s WHERE enrollment_id=%s;", (safe_date(new_date), enrollment_id))
    conn.commit()
    cur.close()
    conn.close()

# 你可以在文件最后加：
if __name__ == "__main__":
    get_all_enrollments()
    add_student("测试学员")
    delete_enrollment(2)
    update_finish_date(3, '2025-08-31')
