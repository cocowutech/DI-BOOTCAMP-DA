import psycopg2

# 替换为你自己的数据库连接信息
conn = psycopg2.connect(
    dbname="postgres",         # 默认数据库名
    user="postgres",           # 你的用户名
    password="941125",         # 你的密码
    host="localhost",          # 本地数据库
    port="5432"                # 默认端口
)

cursor = conn.cursor()

# 测试查询
cursor.execute("SELECT version();")
version = cursor.fetchone()
print("Connected! PostgreSQL version:", version)



cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
print(cursor.fetchall())  # 显示所有你创建的表

cursor.close()
conn.close()