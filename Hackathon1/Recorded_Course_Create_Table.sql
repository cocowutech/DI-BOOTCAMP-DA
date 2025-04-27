DROP TABLE IF EXISTS enrollment_tas, enrollments, tas, sales, courses, students CASCADE;

-- 学生表
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    dropout BOOLEAN DEFAULT FALSE
);

-- 课程表
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL
);

-- 渠道表
CREATE TABLE sales (
    sales_id SERIAL PRIMARY KEY,
    sales_name VARCHAR(50) UNIQUE NOT NULL,   -- 推荐人（唯一）
    channel_type VARCHAR(30)                  -- 介绍渠道
);

-- 助教表
CREATE TABLE tas (
    ta_id SERIAL PRIMARY KEY,
    ta_name VARCHAR(50) NOT NULL
);

-- 报名主表
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
    course_id INTEGER NOT NULL REFERENCES courses(course_id),
    sales_id INTEGER REFERENCES sales(sales_id),
    gross_income NUMERIC(10,2),
    book_cost NUMERIC(10,2),
    net_expense NUMERIC(10,2),
    net_profit NUMERIC(10,2),
    status VARCHAR(20) DEFAULT 'active', -- active/dropout/finished
    enrolled_date DATE,
    expected_finish_date DATE
);

-- 报名-助教关联表
CREATE TABLE enrollment_tas (
    enrollment_id INTEGER REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    ta_id INTEGER REFERENCES tas(ta_id),
    ta_fee NUMERIC(10,2),
    PRIMARY KEY (enrollment_id, ta_id)
);
