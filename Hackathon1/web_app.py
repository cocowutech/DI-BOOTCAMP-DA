import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime, date
from db_config import get_conn  # 直接用你已有的数据库连接模块

# ===================== 数据交互核心 =====================

def load_students():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.enrollment_id, s.student_name, c.course_name, e.status,
               e.enrolled_date, e.expected_finish_date
        FROM enrollments e
        JOIN students s ON e.student_id=s.student_id
        JOIN courses c ON e.course_id=c.course_id
        ORDER BY e.enrollment_id
    """)
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=['报名ID', '学生姓名', '课程', '状态', '开营日期', '预计结营日期'])
    cur.close()
    conn.close()
    return df

def get_courses():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT course_name FROM courses ORDER BY course_id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [r[0] for r in rows]

def get_students():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT student_name FROM students ORDER BY student_id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [r[0] for r in rows]

def get_student_id(student_name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT student_id FROM students WHERE student_name=%s", (student_name,))
    student_id = cur.fetchone()
    cur.close()
    conn.close()
    return student_id[0] if student_id else None

def get_course_id(course_name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT course_id FROM courses WHERE course_name=%s", (course_name,))
    course_id = cur.fetchone()
    cur.close()
    conn.close()
    return course_id[0] if course_id else None

def add_enrollment(student_name, course_name, start_date, finish_date):
    student_id = get_student_id(student_name)
    course_id = get_course_id(course_name)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO enrollments (student_id, course_id, sales_id, gross_income, book_cost, net_expense, net_profit, status, enrolled_date, expected_finish_date)
        VALUES (%s, %s, NULL, 0, 0, 0, 0, 'active', %s, %s)
    """, (student_id, course_id, start_date, finish_date))
    conn.commit()
    cur.close()
    conn.close()

def delete_enrollment(enrollment_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM enrollments WHERE enrollment_id=%s", (enrollment_id,))
    conn.commit()
    cur.close()
    conn.close()

def update_enrollment(enrollment_id, start_date, finish_date, status):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE enrollments SET enrolled_date=%s, expected_finish_date=%s, status=%s WHERE enrollment_id=%s
    """, (start_date, finish_date, status, enrollment_id))
    conn.commit()
    cur.close()
    conn.close()

# ===================== 页面部分 =====================

st.set_page_config(page_title="学生进度管理", layout="wide")
st.title("🎓 录播课学生数据管理系统")

# 1. 数据表及进度条
df = load_students()
df['开营日期'] = pd.to_datetime(df['开营日期']).dt.date
df['预计结营日期'] = pd.to_datetime(df['预计结营日期']).dt.date

# 计算进度百分比
def progress_days(row):
    if pd.isna(row['开营日期']) or pd.isna(row['预计结营日期']):
        return 0.0
    total = (row['预计结营日期'] - row['开营日期']).days
    done = (min(date.today(), row['预计结营日期']) - row['开营日期']).days
    return max(0, min(done / total, 1)) if total > 0 else 0.0

df['进度%'] = df.apply(progress_days, axis=1)
df['进度条'] = df['进度%'].apply(lambda x: f"{x*100:.1f}%")

st.subheader("当前学生数据表（含进度条）")
st.dataframe(df[['报名ID', '学生姓名', '课程', '状态', '开营日期', '预计结营日期', '进度条']])

st.subheader("学生在读进度可视化")
for i, row in df.iterrows():
    st.write(f"{row['学生姓名']} - {row['课程']}")
    st.progress(row['进度%'])

st.markdown("---")

# 2. 增删改查功能区

tab1, tab2, tab3 = st.tabs(["➕ 添加报名", "📝 编辑报名", "❌ 删除报名"])

with tab1:
    st.header("添加新报名")
    student_name = st.selectbox("选择学生", get_students(), key="add_student")
    course_name = st.selectbox("选择课程", get_courses(), key="add_course")
    start_date = st.date_input("开营日期", value=date.today(), key="add_start")
    finish_date = st.date_input("预计结营日期", value=date.today(), key="add_finish")
    if st.button("添加报名"):
        add_enrollment(student_name, course_name, start_date, finish_date)
        st.success("报名已添加！请刷新页面查看。")

with tab2:
    st.header("编辑报名")
    enroll_ids = df['报名ID'].tolist()
    edit_id = st.selectbox("选择报名ID", enroll_ids, key="edit_id")
    enroll_row = df[df['报名ID'] == edit_id].iloc[0]
    new_start = st.date_input("新开营日期", value=enroll_row['开营日期'], key="edit_start")
    new_finish = st.date_input("新预计结营日期", value=enroll_row['预计结营日期'], key="edit_finish")
    new_status = st.selectbox("状态", ["active", "dropout"], index=0 if enroll_row['状态']=="active" else 1, key="edit_status")
    if st.button("保存修改"):
        update_enrollment(edit_id, new_start, new_finish, new_status)
        st.success("报名信息已更新！请刷新页面查看。")

with tab3:
    st.header("删除报名")
    del_id = st.selectbox("选择要删除的报名ID", df['报名ID'].tolist(), key="del_id")
    if st.button("删除报名"):
        delete_enrollment(del_id)
        st.warning("报名已删除！请刷新页面查看。")

st.caption("提示：所有操作都是实时生效，刷新页面可看到最新数据。")

