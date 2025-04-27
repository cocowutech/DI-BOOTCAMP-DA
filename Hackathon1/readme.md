
---

## 快速开始 Quick Start

1. **环境准备 Environment Setup**
   - 创建并激活 Python 虚拟环境（建议venv/conda）
   - Create and activate a Python virtual environment (`venv` or `conda` recommended)
   - 安装依赖 Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **配置数据库 Configure Database**
   - 修改 `db_config.py` 为你的 PostgreSQL 账号密码及数据库名
   - Modify `db_config.py` with your PostgreSQL credentials and database name.

3. **建表 Create Tables**
   - 在 pgAdmin/psql 中运行提供的 `CREATE TABLE` 脚本（见辅助文档或数据库脚本）
   - Run the provided `CREATE TABLE` SQL script in pgAdmin/psql.

4. **批量导入数据 Batch Import Data**
   - 将所有 CSV 文件放入 `data/` 文件夹
   - Place all CSV files in the `data/` folder
   - 执行批量导入脚本 Run batch import script:
     ```bash
     python import_data.py
     ```

5. **增删改查 CRUD 操作**
   - 用 `crud.py` 示例脚本体验常见数据操作
   - Use `crud.py` for common create/read/update/delete operations

6. **数据分析与可视化 Analysis & Visualization**
   - 执行分析脚本 Run analysis script:
     ```bash
     python analysis.py
     ```
   - 自动生成中英双语 Excel 报表、条形图
   - Generates bilingual Excel reports and bar charts automatically.

---

## 依赖包 Dependencies

- pandas
- psycopg2
- openpyxl
- matplotlib

---

## 主要功能 Key Features

- 多表结构建模，支持教培业务核心数据拆分
- 支持所有数据的批量导入和去重
- 增删改查操作简洁易用
- 课程、销售/渠道利润排名自动统计
- 报表导出、条形图一键可视化
- 全流程中英双语支持（表头、图表、输出报表）
- 代码结构清晰，方便二次开发/交接/展示

---

## 贡献和反馈 Contribution & Feedback

如有建议、BUG或想扩展本系统功能，欢迎PR或发Issue！  
For suggestions, bug reports, or feature requests, feel free to submit a PR or open an issue.

---

祝你使用愉快，项目大卖！  
Wish you a great success with your project!
