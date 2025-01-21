import sys
sys.path.insert(0, 'D:/github/vanna/src')

try:
    from vanna.openai import OpenAI_Chat
    from vanna.chromadb import ChromaDB_VectorStore
    import yaml  # 添加 yaml 导入
except ImportError as e:
    print(f"导入错误: {e}")
    print("请确保已安装所需的包：")
    print("pip install openai chromadb pyyaml")
    sys.exit(1)

###########################################
# 第一部分：初始化 MyVanna 并连接数据库
###########################################

# 读取配置文件
try:
    with open('config.yaml', 'r', encoding='utf-8') as file:  # 明确指定 UTF-8 编码
        config = yaml.safe_load(file)
except Exception as e:
    print(f"读取配置文件失败: {e}")
    sys.exit(1)

class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)
        
    def search_tables_metadata(self, query: str) -> list:
        """搜索表元数据的方法"""
        return []

# 初始化 Vanna 实例
vn = MyVanna(config={
    'api_key': config['openai']['api_key'],  # 从配置文件读取 API 密钥
    'model': config['openai']['model']       # 从配置文件读取模型设置
})

# 连接到 PostgreSQL 数据库
vn.connect_to_postgres(
    host=config['database']['host'],
    dbname=config['database']['dbname'],
    user=config['database']['user'],
    password=config['database']['password'],
    port=config['database']['port']
)

###########################################
# 第二部分：添加训练材料（可选）
###########################################

# # You can remove training data if there's obsolete/incorrect information. 
# # 获取所有训练数据
# training_data = vn.get_training_data()

# # 遍历所有训练数据并删除
# for index, row in training_data.iterrows():
#     if 'id' in row:
#         try:
#             vn.remove_training_data(id=row['id'])
#             print(f"已删除训练数据: {row['id']}")
#         except Exception as e:
#             print(f"删除训练数据 {row['id']} 时出错: {e}")

# # 获取数据库表结构信息
# df_information_schema = vn.run_sql("""
#     SELECT * 
#     FROM INFORMATION_SCHEMA.COLUMNS 
#     WHERE table_catalog = 'postgres' 
#     AND table_schema = 't_404520320'
# """)

# # 生成训练计划
# plan = vn.get_training_plan_generic(df_information_schema)
# print("训练计划：", plan)

# # 执行训练
# vn.train(plan=plan)

# # 添加其他训练数据示例
# vn.train(ddl="""
#     CREATE TABLE IF NOT EXISTS example_table (
#         id INT PRIMARY KEY,
#         name VARCHAR(100),
#         age INT
#     )
# """)

# # 添加业务术语文档
# vn.train(documentation="列出数据库中所有的表")

# # 添加示例SQL查询
# vn.train(sql="SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE table_catalog = 'postgres' AND table_schema = 't_404520320'")

# 查看当前训练数据
training_data = vn.get_training_data()
print("当前训练数据：", training_data)

###########################################
# 第三部分：运行 Flask 前端应用
###########################################

from vanna.flask import VannaFlaskApp

# 配置 Flask 应用
app = VannaFlaskApp(
    vn=vn,                                       # Vanna 实例
    debug=True,                                  # 开启调试模式
    logo="https://img.vanna.ai/vanna-flask.svg", # 设置 Logo
    title="Welcome to Vanna.AI",                 # 设置标题
    subtitle="Your AI-powered SQL Assistant",    # 设置副标题
    
    # 功能开关配置
    show_training_data=True,    # 显示训练数据
    allow_llm_to_see_data=True, # 允许 LLM 查看数据
    suggested_questions=True,    # 启用建议问题
    sql=True,                   # 启用 SQL 查询
    table=True,                 # 启用表格显示
    csv_download=True,          # 启用 CSV 下载
    chart=True,                 # 启用图表功能
    redraw_chart=True,          # 启用重绘图表
    auto_fix_sql=True,          # 启用 SQL 自动修复
    ask_results_correct=True,   # 启用结果验证
    followup_questions=True,    # 启用后续问题
    summarization=True          # 启用总结功能
)

# 启动应用
if __name__ == '__main__':
    app.run()
