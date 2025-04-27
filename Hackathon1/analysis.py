from db_config import get_conn
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei', 'Heiti TC', 'PingFang', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 中英双语映射
col_bilingual = {
    '课程': '课程 (Course)',
    '报名人数': '报名人数 (Enrollments)',
    '毛流水': '毛流水 (Gross Income)',
    '净利润': '净利润 (Net Profit)',
    '净利润占比%': '净利润占比% (Net Profit Ratio %)',
    '推荐人': '推荐人 (Sales)',
}

course_bilingual = {
    'PET-60天': 'PET-60天 (PET, 60D)',
    'KET-136天': 'KET-136天 (KET, 136D)',
    'FCE-63天': 'FCE-63天 (FCE, 63D)',
    'PET-96天': 'PET-96天 (PET, 96D)',
    'KET-160': 'KET-160 (KET, 160D)',
    'KET-72天': 'KET-72天 (KET, 72D)',
}

def course_profit_ranking_with_ratio_excel():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    SELECT c.course_name,
           COUNT(DISTINCT e.enrollment_id) as num_students,
           SUM(e.gross_income) as total_gross,
           SUM(e.net_profit) as course_profit
    FROM enrollments e
    JOIN courses c ON e.course_id = c.course_id
    WHERE e.status='active'
    GROUP BY c.course_name
    ORDER BY course_profit DESC
    """)
    rows = cur.fetchall()
    df_course = pd.DataFrame(rows, columns=['课程', '报名人数', '毛流水', '净利润'])

    # 总利润
    cur.execute("SELECT SUM(e.net_profit) FROM enrollments e WHERE e.status='active'")
    total_profit = cur.fetchone()[0] or 0
    df_course['净利润占比%'] = df_course['净利润'].astype(float) / float(total_profit) * 100 if total_profit else 0

    # 应用双语列名和内容
    df_course = df_course.rename(columns=col_bilingual)
    if '课程 (Course)' in df_course.columns:
        df_course['课程 (Course)'] = df_course['课程 (Course)'].map(lambda x: course_bilingual.get(x, x))

    cur.close()
    conn.close()
    return df_course, total_profit

def top_sales_analysis_excel(topn=10):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    SELECT sa.sales_name,
           COUNT(DISTINCT e.enrollment_id) as num_students,
           SUM(e.gross_income) as total_gross,
           SUM(e.net_profit) as total_profit
    FROM enrollments e
    JOIN sales sa ON e.sales_id = sa.sales_id
    WHERE e.status='active'
    GROUP BY sa.sales_name
    ORDER BY total_profit DESC
    LIMIT %s
    """, (topn,))
    rows = cur.fetchall()
    df_sales = pd.DataFrame(rows, columns=['推荐人', '报名人数', '毛流水', '净利润'])
    df_sales = df_sales.rename(columns=col_bilingual)
    cur.close()
    conn.close()
    return df_sales

if __name__ == "__main__":
    # 1. 课程分析
    df_course, total_profit = course_profit_ranking_with_ratio_excel()
    print("\n【课程利润分析（Course Profit）】\n")
    print(df_course.to_string(index=False))
    print(f"\n总利润 Total Net Profit: {total_profit}\n")

    # 2. Top销售
    df_sales = top_sales_analysis_excel(10)
    print("【Top销售分析（Top Sales）】\n")
    print(df_sales.to_string(index=False))

    # 3. 输出到Excel
    with pd.ExcelWriter('analysis_report_bilingual.xlsx', engine='openpyxl') as writer:
        df_course.to_excel(writer, index=False, sheet_name='课程利润_Profit')
        df_sales.to_excel(writer, index=False, sheet_name='Top销售_TopSales')
    print("\nExcel已保存为 analysis_report_bilingual.xlsx")

    # 4. 课程条形图
    plt.figure(figsize=(10,5))
    plt.bar(df_course['课程 (Course)'], df_course['净利润 (Net Profit)'])
    plt.xlabel('课程 (Course)')
    plt.ylabel('净利润 (Net Profit)')
    plt.title('各课程净利润排行 (Net Profit by Course)')
    plt.tight_layout()
    plt.savefig("course_profit_bar_bilingual.png")
    plt.show()

    # 5. Top销售条形图
    plt.figure(figsize=(10,5))
    plt.bar(df_sales['推荐人 (Sales)'], df_sales['净利润 (Net Profit)'])
    plt.xlabel('推荐人 (Sales)')
    plt.ylabel('净利润 (Net Profit)')
    plt.title('Top销售净利润排行 (Top Sales by Net Profit)')
    plt.tight_layout()
    plt.savefig("top_sales_profit_bar_bilingual.png")
    plt.show()
