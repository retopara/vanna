import sys
sys.path.insert(0, 'D:/github/vanna/src') # remove if you have a differen path for vanna

try:
    from vanna.openai import OpenAI_Chat
    from vanna.chromadb import ChromaDB_VectorStore
    import yaml  # 添加 yaml 导入
    from vanna.qianwen import QianWenAI_Embeddings
    from openai import OpenAI
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
    # 读取主配置文件
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    
    # 读取API密钥配置文件
    with open('api_secret.yaml', 'r', encoding='utf-8') as file:
        api_secret = yaml.safe_load(file)
    
    # 将API密钥添加到配置中
    if 'openai' not in config:
        config['openai'] = {}
    config['openai']['api_key'] = api_secret['openai']['api_key']
    
    # 添加千问API密钥
    if 'qianwen' not in config:
        config['qianwen'] = {}
    config['qianwen']['api_key'] = api_secret['qianwen']['api_key']
    
    # 添加 deepseek 配置
    if 'deepseek' not in config:
        config['deepseek'] = {}
    # 从 api_secret.yaml 读取 API 密钥
    config['deepseek']['api_key'] = api_secret['deepseek']['api_key']
    # 确保其他 deepseek 配置项存在
    if 'model' not in config['deepseek']:
        config['deepseek']['model'] = 'deepseek-chat'
    if 'base_url' not in config['deepseek']:
        config['deepseek']['base_url'] = 'https://api.deepseek.com'
    if 'temperature' not in config['deepseek']:
        config['deepseek']['temperature'] = 0.7
    
    print("成功加载 deepseek 配置:")
    print(f"- Model: {config['deepseek']['model']}")
    print(f"- Base URL: {config['deepseek']['base_url']}")
    print(f"- Temperature: {config['deepseek']['temperature']}")
    
except Exception as e:
    print(f"读取配置文件失败: {e}")
    sys.exit(1)

# 初始化 deepseek 客户端
deepseek_client = OpenAI(
    api_key=config['deepseek']['api_key'],
    base_url=config['deepseek']['base_url']
)

class MyVanna(ChromaDB_VectorStore, OpenAI_Chat, QianWenAI_Embeddings):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, client=deepseek_client, config=config)  # 使用 deepseek 客户端
        QianWenAI_Embeddings.__init__(self, config=config)
        
    def search_tables_metadata(self, query: str) -> list:
        """搜索表元数据的方法"""
        return []
    
# 初始化 Vanna 实例
vn = MyVanna(config={
    'api_key': config['openai']['api_key'],
    'model': config['deepseek']['model'],
    'qianwen_api_key': config['qianwen']['api_key'],
    'embedding_model': config['embedding']['model'],
    'base_url': config['embedding']['base_url'],
    'deepseek': {
        'api_key': config['deepseek']['api_key'],
        'model': config['deepseek']['model'],
        'base_url': config['deepseek']['base_url'],
        'temperature': config['deepseek']['temperature']
    }
})

# 连接到 PostgreSQL 数据库
vn.connect_to_postgres(
    host=config['database']['host'],
    dbname=config['database']['dbname'],
    user=config['database']['user'],
    password=config['database']['password'],
    port=config['database']['port'],
    schema=config['database'].get('schema')  # 删除默认值 'public'
)

###########################################
# 第二部分：添加训练材料（可选）
###########################################

# # You can remove training data if there's obsolete/incorrect information. 
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
#     SELECT table_catalog, 'standard_model' as table_schema, table_name, column_name, ordinal_position, column_default, is_nullable, data_type
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
from markupsafe import Markup
from flask import redirect, url_for, request, jsonify
import traceback

class CustomVannaFlaskApp(VannaFlaskApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 添加获取模型列表的API端点
        @self.flask_app.route('/api/models')
        def get_models():
            try:
                sql = """
                SELECT id, db_file_name as model_name, create_by as created_by, 
                       create_date as created_date, db_file_path as schema_name
                FROM postgres.public.scm_project_model
                """
                print(f"执行SQL查询: {sql}")
                df = vn.run_sql(sql)
                print(f"查询结果: {df}")
                result = df.to_json(orient='records', date_format='iso')
                print(f"JSON结果: {result}")
                return result
            except Exception as e:
                print(f"获取模型列表时出错: {str(e)}")
                return jsonify({'error': str(e)}), 500

        # 添加检查 schema 状态的 API 端点
        @self.flask_app.route('/api/check_schema')
        def check_schema():
            print("\n=== 开始检查 Schema 状态 ===")
            try:
                # 检查数据库连接
                if not hasattr(vn, 'connection') or vn.connection is None:
                    print("检查结果: 数据库连接不存在")
                    return jsonify({
                        'has_schema': False,
                        'message': '请选择模型'
                    })
                
                # 获取当前 schema
                current_schema = None
                if hasattr(vn, 'schema'):
                    current_schema = vn.schema
                print(f"当前 Schema: {current_schema}")
                
                # 检查 schema 是否存在且是否符合 "t_" 开头的格式
                if not current_schema:  # 明确检查 None 或空字符串的情况
                    print("检查结果: Schema 为空")
                    return jsonify({
                        'has_schema': False,
                        'message': '请选择模型'
                    })
                    
                if not current_schema.startswith('t_'):
                    print(f"检查结果: Schema '{current_schema}' 不符合't_'开头的格式要求")
                    return jsonify({
                        'has_schema': False,
                        'message': '请选择模型'
                    })
                
                print(f"检查结果: Schema '{current_schema}' 验证通过")
                return jsonify({
                    'has_schema': True,
                    'schema': current_schema
                })
            except Exception as e:
                print(f"检查过程出现异常: {str(e)}")
                print(f"异常详细信息: {traceback.format_exc()}")
                return jsonify({
                    'has_schema': False,
                    'message': '请选择模型'
                })
            finally:
                print("=== Schema 检查完成 ===\n")

        # 修改主页面的 HTML 内容
        @self.flask_app.route('/')
        def index():
            return """
            <!doctype html>
            <html lang="en" translate>
              <head>
                <meta charset="UTF-8" />
                <link rel="icon" type="image/svg+xml" href="/vanna.svg" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@350&display=swap" rel="stylesheet">
                <script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
                <title>Vanna.AI</title>
                <script type="module" crossorigin src="/assets/index-35bab439.js"></script>
                <link rel="stylesheet" href="/assets/index-f228f78f.css">
                <script>
                    // 在页面加载前检查 schema 状态
                    (async function() {
                        try {
                            const response = await fetch('/api/check_schema');
                            const data = await response.json();
                            if (!data.has_schema) {
                                alert(data.message);
                                window.location.href = '/schema_select';
                                return;  // 阻止页面继续加载
                            }
                        } catch (error) {
                            console.error('Error checking schema:', error);
                            alert('检查模型状态时出错');
                            window.location.href = '/schema_select';
                        }
                    })();
                </script>
              </head>
              <body class="bg-white dark:bg-slate-900">
                <div id="app"></div>
                <div style="position: fixed; top: 20px; left: 50%; transform: translateX(-50%); z-index: 1000;">
                  <a href="/schema_select" 
                     style="display: inline-block; padding: 8px 16px; 
                            background-color: #0d6efd; color: white; 
                            text-decoration: none; border-radius: 4px;
                            font-family: system-ui, -apple-system, sans-serif;
                            font-size: 14px;">
                    选择模型
                  </a>
                </div>
              </body>
            </html>
            """

        # 添加模型搜索的API端点
        @self.flask_app.route('/api/search_models')
        def search_models():
            search_term = request.args.get('term', '').lower()
            try:
                sql = f"""
                SELECT id, db_file_name as model_name, create_by as created_by, 
                       create_date as created_date, db_file_path as schema_name
                FROM postgres.public.scm_project_model
                WHERE LOWER(id::text) LIKE '%%{search_term}%%' 
                   OR LOWER(db_file_name) LIKE '%%{search_term}%%'
                   OR LOWER(create_by) LIKE '%%{search_term}%%'
                   OR LOWER(db_file_path) LIKE '%%{search_term}%%'
                """
                print(f"执行搜索SQL: {sql}")
                df = vn.run_sql(sql)  # 移除了参数化查询
                print(f"搜索结果: {df}")
                result = df.to_json(orient='records', date_format='iso')
                print(f"JSON搜索结果: {result}")
                return result
            except Exception as e:
                print(f"搜索模型时出错: {str(e)}")
                return jsonify({'error': str(e)}), 500

        # 添加设置选中模型的API端点
        @self.flask_app.route('/api/set_model', methods=['POST'])
        def set_model():
            model_data = request.json
            if model_data and 'schema_name' in model_data:
                schema = model_data['schema_name']
                print(f"\n正在切换到新的 schema: {schema}")
                
                # 重新连接数据库并指定新的 schema
                vn.connect_to_postgres(
                    host=config['database']['host'],
                    dbname=config['database']['dbname'],
                    user=config['database']['user'],
                    password=config['database']['password'],
                    port=config['database']['port'],
                    schema=schema
                )
                
                # 更新 VannaBase 的 initial_prompt，添加更详细的 SQL 格式指导
                # vn.static_documentation = f"""
                # Important SQL formatting rules:
                # 2. Always using double quotes around table names if there are uppercase letters.
                # 3. Example: SELECT * FROM {schema}."CustomerOrders".
                # 4. All queries must be executed within schema: {schema}
                # """
                
                print(f"数据库连接已更新:")
                print(f"- Schema: {schema}")
                print(f"- Host: {config['database']['host']}")
                print(f"- Database: {config['database']['dbname']}")
                print(f"- User: {config['database']['user']}")
                print(f"- Port: {config['database']['port']}")
                print("连接更新完成\n")
                
                return jsonify({
                    'success': True,
                    'message': f'已切换到 schema: {schema}'
                })
            return jsonify({
                'error': 'Invalid model data',
                'message': '未提供有效的 schema 信息'
            }), 400

        # 添加 schema 选择页面路由
        @self.flask_app.route('/schema_select')
        def schema_select():
            return """
            <html>
                <head>
                    <title>Schema Select</title>
                    <style>
                        body { font-family: Arial, sans-serif; padding: 20px; }
                        h1 { color: #333; }
                        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
                                background-color: rgba(0,0,0,0.5); }
                        .modal-content { background-color: white; margin: 15% auto; padding: 20px; 
                                       width: 80%; border-radius: 5px; }
                        .search-container { display: flex; gap: 10px; margin-bottom: 15px; }
                        .search-box { flex-grow: 1; padding: 8px; }
                        .search-button { padding: 8px 16px; cursor: pointer; }
                        .models-table { width: 100%; border-collapse: collapse; }
                        .models-table th, .models-table td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                        .models-table tr:hover { background-color: #f5f5f5; cursor: pointer; }
                        .selected { background-color: #e0e0e0 !important; }
                        .button-container { margin-top: 20px; text-align: right; }
                        .button-container button { margin-left: 10px; padding: 8px 16px; cursor: pointer; }
                    </style>
                    <script>
                        let selectedModel = null;
                        
                        function openModelDialog() {
                            document.getElementById('modelModal').style.display = 'block';
                            loadModels();
                        }
                        
                        function closeModelDialog() {
                            document.getElementById('modelModal').style.display = 'none';
                        }
                        
                        async function loadModels() {
                            try {
                                const response = await fetch('/api/models');
                                if (!response.ok) {
                                    throw new Error(`HTTP error! status: ${response.status}`);
                                }
                                const models = await response.json();
                                displayModels(models);
                            } catch (error) {
                                console.error('Error loading models:', error);
                                alert('加载模型列表失败: ' + error.message);
                            }
                        }
                        
                        function displayModels(models) {
                            const tbody = document.querySelector('.models-table tbody');
                            tbody.innerHTML = models.map(model => `
                                <tr class="${selectedModel && selectedModel.id === model.id ? 'selected' : ''}" 
                                    onclick="selectModel(this, ${JSON.stringify(model).replace(/"/g, '&quot;')})">
                                    <td>${model.id || ''}</td>
                                    <td>${model.model_name || ''}</td>
                                    <td>${model.created_by || ''}</td>
                                    <td>${model.created_date ? new Date(model.created_date).toLocaleString() : ''}</td>
                                    <td>${model.schema_name || ''}</td>
                                </tr>
                            `).join('');
                        }
                        
                        function selectModel(row, model) {
                            // 移除之前选中行的高亮
                            document.querySelectorAll('.models-table tr').forEach(tr => {
                                tr.classList.remove('selected');
                            });
                            
                            // 添加新选中行的高亮
                            row.classList.add('selected');
                            selectedModel = model;
                            
                            // 更新选中状态显示
                            console.log('已选中模型:', model);
                        }
                        
                        async function confirmModelSelection() {
                            if (!selectedModel) {
                                alert('请先选择一个模型');
                                return;
                            }
                            
                            try {
                                const response = await fetch('/api/set_model', {
                                    method: 'POST',
                                    headers: { 'Content-Type': 'application/json' },
                                    body: JSON.stringify(selectedModel)
                                });
                                
                                if (response.ok) {
                                    closeModelDialog();
                                    document.getElementById('selectedModelInfo').textContent = 
                                        `已选择模型: ${selectedModel.model_name} (Schema: ${selectedModel.schema_name})`;
                                } else {
                                    throw new Error('设置模型失败');
                                }
                            } catch (error) {
                                console.error('Error setting model:', error);
                                alert('设置模型失败: ' + error.message);
                            }
                        }
                        
                        async function searchModels() {
                            const searchTerm = document.getElementById('searchInput').value.trim();
                            if (!searchTerm) {
                                loadModels();  // 如果搜索词为空，加载所有模型
                                return;
                            }
                            
                            try {
                                const response = await fetch(`/api/search_models?term=${encodeURIComponent(searchTerm)}`);
                                if (!response.ok) {
                                    throw new Error(`HTTP error! status: ${response.status}`);
                                }
                                const models = await response.json();
                                displayModels(models);
                            } catch (error) {
                                console.error('Error searching models:', error);
                                alert('搜索模型失败: ' + error.message);
                            }
                        }

                        // 添加回车键搜索支持
                        function handleSearchKeyPress(event) {
                            if (event.key === 'Enter') {
                                searchModels();
                            }
                        }
                    </script>
                </head>
                <body>
                    <h1>Schema Select</h1>
                    <button onclick="openModelDialog()">选择模型</button>
                    <div id="selectedModelInfo"></div>
                    <form action="/" method="get">
                        <button type="submit">继续到主页面</button>
                    </form>
                    
                    <div id="modelModal" class="modal">
                        <div class="modal-content">
                            <h2>选择模型</h2>
                            <div class="search-container">
                                <input type="text" id="searchInput" class="search-box" 
                                       placeholder="输入关键词搜索模型..." 
                                       onkeypress="handleSearchKeyPress(event)">
                                <button onclick="searchModels()" class="search-button">搜索</button>
                            </div>
                            <table class="models-table">
                                <thead>
                                    <tr>
                                        <th>模型ID</th>
                                        <th>模型名称</th>
                                        <th>创建人</th>
                                        <th>创建时间</th>
                                        <th>Schema名称</th>
                                    </tr>
                                </thead>
                                <tbody></tbody>
                            </table>
                            <div class="button-container">
                                <button onclick="confirmModelSelection()">确定</button>
                                <button onclick="closeModelDialog()">取消</button>
                            </div>
                        </div>
                    </div>
                </body>
            </html>
            """
            
        @self.flask_app.route('/select_model', methods=['POST'])
        def select_model():
            data = request.get_json()
            model_id = data.get('model_id')
            
            # 获取模型信息
            sql = """
            SELECT db_file_path as schema_name
            FROM postgres.public.scm_project_model
            WHERE id = %s
            """
            df = vn.run_sql(sql, (model_id,))
            
            if not df.empty:
                schema = df['schema_name'].iloc[0]
                # 设置 schema 到 vn 实例中
                vn.schema = schema  # 需要在 VannaBase 类中添加 schema 属性
                
                return jsonify({
                    'status': 'success',
                    'message': f'已选择模型 {model_id}，使用 schema: {schema}'
                })
            else:
                return jsonify({
                    'status': 'error',
                    'message': '未找到指定的模型'
                }), 404

# 配置 Flask 应用
app = CustomVannaFlaskApp(
    vn=vn,
    debug=True,
    
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
    print("Your app is running at:")
    print("http://localhost:8084/schema_select")  # 更新显示的URL
    app.flask_app.debug = True  # 显式设置 Flask 应用的 debug 模式
    app.run(port=8084)

