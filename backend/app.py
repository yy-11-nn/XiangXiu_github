import sys
if sys.version_info >= (3, 10):
    import collections.abc
    import collections
    if not hasattr(collections, 'MutableSet'):
        collections.MutableSet = collections.abc.MutableSet
    if not hasattr(collections, 'MutableMapping'):
        collections.MutableMapping = collections.abc.MutableMapping
    if not hasattr(collections, 'Callable'):
        collections.Callable = collections.abc.Callable

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import hashlib
from functools import wraps
from config import config
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 创建Flask应用
app = Flask(__name__)

# AI 助手配置（纯关键词检索模式）
VECTOR_SEARCH_AVAILABLE = False
vector_collection = None
embedding_model = None

# 加载配置
app_config = config[os.getenv('FLASK_ENV') or 'default']
app.config.from_object(app_config)

# 初始化扩展
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 添加安全响应头
@app.after_request
def add_security_headers(response):
    # 允许 iframe 嵌入（开发环境使用，生产环境建议限制域名）
    response.headers.pop('X-Frame-Options', None)
    # 内容安全策略 - 允许本地开发环境
    response.headers['Content-Security-Policy'] = "frame-ancestors 'self' http://localhost:* http://127.0.0.1:* https://*;"
    # 其他安全头
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# 密码加密函数
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 数据库模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    # 关联
    cart_items = db.relationship('CartItem', backref='user', lazy=True)
    collect_items = db.relationship('CollectItem', backref='user', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    # 关联
    cart_items = db.relationship('CartItem', backref='product', lazy=True)
    collect_items = db.relationship('CollectItem', backref='product', lazy=True)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class CollectItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    # 唯一约束：用户不能重复收藏同一商品
    __table_args__ = (db.UniqueConstraint('user_id', 'product_id', name='_user_product_uc'),)

class KnowledgeNode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    source_file = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class KeywordReply(db.Model):
    """关键词回复表 - 用于AI助手的关键词匹配"""
    __tablename__ = 'keyword_reply'
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(200), nullable=False)  # 关键词，多个词用逗号分隔
    reply_content = db.Column(db.Text, nullable=False)   # 回复内容
    category = db.Column(db.String(100), nullable=True)  # 分类（可选）
    priority = db.Column(db.Integer, default=0)          # 优先级，数字越大越优先
    is_active = db.Column(db.Boolean, default=True)      # 是否启用
    match_type = db.Column(db.String(20), default='contains')  # 匹配类型：exact(精确), contains(包含), fuzzy(模糊)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class KnowledgeRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_node_id = db.Column(db.Integer, db.ForeignKey('knowledge_node.id'), nullable=False)
    target_node_id = db.Column(db.Integer, db.ForeignKey('knowledge_node.id'), nullable=False)
    relationship_type = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    # 添加关系定义
    source_node = db.relationship('KnowledgeNode', foreign_keys=[source_node_id], backref='source_relationships')
    target_node = db.relationship('KnowledgeNode', foreign_keys=[target_node_id], backref='target_relationships')

# 3D模型标签关联表
model_tags = db.Table('model_tags',
    db.Column('model_id', db.Integer, db.ForeignKey('model3d.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('model_tag.id'), primary_key=True)
)

class Model3D(db.Model):
    __tablename__ = 'model3d'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(255), nullable=False)
    file_size = db.Column(db.Integer, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    # 关联
    tags = db.relationship('ModelTag', secondary=model_tags, backref='models')

class ModelTag(db.Model):
    __tablename__ = 'model_tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

# 管理权限检查装饰器
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login_page'))
        # 检查是否为管理员
        if not session.get('is_admin'):
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated_function

# 根路径重定向到登录页面
@app.route('/')
def root_redirect():
    return redirect(url_for('login_page'))

# 登录页面路由
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# 登录处理路由
@app.route('/login', methods=['POST'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return render_template('login.html', error='请输入用户名和密码')
    
    # 检查是否为硬编码管理员账户
    if username == 'admin' and password == 'admin123':
        session['user_id'] = 0
        session['username'] = 'admin'
        session['is_admin'] = True
        return redirect(url_for('admin_index'))
    
    # 检查数据库中的用户
    user = User.query.filter_by(username=username).first()
    if user and user.password == hash_password(password) and user.is_admin:
        session['user_id'] = user.id
        session['username'] = user.username
        session['is_admin'] = True
        return redirect(url_for('admin_index'))
    
    return render_template('login.html', error='用户名或密码错误，或无管理权限')

# 登出路由
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))

# API路由
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # 验证数据
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': '缺少必要参数'}), 400
    
    # 检查用户名是否已存在
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': '用户名已存在'}), 400
    
    # 检查邮箱是否已存在
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': '邮箱已被注册'}), 400
    
    # 创建新用户
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hash_password(data['password'])
    )
    
    # 保存到数据库
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': '注册成功', 'user_id': new_user.id}), 201

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        # 验证数据
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'message': '缺少必要参数'}), 400
        
        # 查找用户
        user = User.query.filter_by(username=data['username']).first()
        
        # 验证用户和密码
        if not user or user.password != hash_password(data['password']):
            return jsonify({'message': '用户名或密码错误'}), 401
        
        # 返回登录成功信息，包括用户ID和是否为管理员
        return jsonify({'message': '登录成功', 'user_id': user.id, 'is_admin': user.is_admin}), 200
    except Exception as e:
        print(f"[错误] 登录接口异常: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'message': f'服务器内部错误: {str(e)}'}), 500

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_admin': user.is_admin,
            'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200

# 产品相关API
@app.route('/api/products', methods=['GET'])
def get_products():
    # 支持按类别筛选
    category = request.args.get('category')
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()
    
    result = []
    for product in products:
        result.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'image': product.image,
            'category': product.category,
            'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200

@app.route('/api/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'image': product.image,
        'category': product.category,
        'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S')
    }), 200

# 购物车相关API
@app.route('/api/cart', methods=['GET'])
def get_cart():
    # 从请求中获取用户ID，实际应用中应该从JWT令牌中获取
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': '缺少用户ID'}), 400
    
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    result = []
    for item in cart_items:
        result.append({
            'id': item.id,
            'user_id': item.user_id,
            'product_id': item.product_id,
            'product_name': item.product.name,
            'product_price': item.product.price,
            'product_image': item.product.image,
            'quantity': item.quantity,
            'total_price': item.product.price * item.quantity,
            'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200

@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    
    if not data.get('user_id') or not data.get('product_id') or not data.get('quantity'):
        return jsonify({'message': '缺少必要参数'}), 400
    
    # 检查商品是否存在
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({'message': '商品不存在'}), 404
    
    # 检查购物车中是否已存在该商品
    existing_item = CartItem.query.filter_by(
        user_id=data['user_id'],
        product_id=data['product_id']
    ).first()
    
    if existing_item:
        # 更新数量
        existing_item.quantity += data['quantity']
        db.session.commit()
        return jsonify({'message': '购物车商品数量已更新', 'item_id': existing_item.id}), 200
    else:
        # 添加新商品到购物车
        new_item = CartItem(
            user_id=data['user_id'],
            product_id=data['product_id'],
            quantity=data['quantity']
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': '商品已添加到购物车', 'item_id': new_item.id}), 201

@app.route('/api/cart/<int:id>', methods=['PUT'])
def update_cart_item(id):
    data = request.get_json()
    cart_item = CartItem.query.get_or_404(id)
    
    if data.get('quantity'):
        cart_item.quantity = data['quantity']
    
    db.session.commit()
    return jsonify({'message': '购物车商品已更新'}), 200

@app.route('/api/cart/<int:id>', methods=['DELETE'])
def remove_from_cart(id):
    cart_item = CartItem.query.get_or_404(id)
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': '商品已从购物车移除'}), 200

# 收藏相关API
@app.route('/api/collect', methods=['GET'])
def get_collect():
    # 从请求中获取用户ID，实际应用中应该从JWT令牌中获取
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': '缺少用户ID'}), 400
    
    collect_items = CollectItem.query.filter_by(user_id=user_id).all()
    result = []
    for item in collect_items:
        result.append({
            'id': item.id,
            'user_id': item.user_id,
            'product_id': item.product_id,
            'product_name': item.product.name,
            'product_price': item.product.price,
            'product_image': item.product.image,
            'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200

@app.route('/api/collect', methods=['POST'])
def add_to_collect():
    data = request.get_json()
    
    if not data.get('user_id') or not data.get('product_id'):
        return jsonify({'message': '缺少必要参数'}), 400
    
    # 检查商品是否存在
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({'message': '商品不存在'}), 404
    
    # 检查是否已收藏
    existing_item = CollectItem.query.filter_by(
        user_id=data['user_id'],
        product_id=data['product_id']
    ).first()
    
    if existing_item:
        return jsonify({'message': '商品已收藏'}), 400
    
    # 添加到收藏
    new_item = CollectItem(
        user_id=data['user_id'],
        product_id=data['product_id']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': '商品已收藏', 'item_id': new_item.id}), 201

@app.route('/api/collect/<int:id>', methods=['DELETE'])
def remove_from_collect(id):
    collect_item = CollectItem.query.get_or_404(id)
    db.session.delete(collect_item)
    db.session.commit()
    return jsonify({'message': '商品已从收藏夹移除'}), 200

# Knowledge Graph API
import csv
import os

@app.route('/api/knowledge/import', methods=['POST'])
def import_knowledge():
    """Import knowledge nodes from CSV files"""
    try:
        data_dir = os.path.join(os.path.dirname(__file__), 'data')
        imported_count = 0
        
        # Process all CSV files in data directory
        for filename in os.listdir(data_dir):
            if filename.endswith('.csv'):
                filepath = os.path.join(data_dir, filename)
                with open(filepath, 'r', encoding='utf-8-sig') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # 处理不同格式的CSV文件
                        category = row.get('类别')
                        content = None
                        
                        # 优先使用"内容"字段，如果没有则使用"详情"字段
                        if row.get('内容'):
                            content = row['内容']
                        elif row.get('详情'):
                            content = row['详情']
                        
                        # 如果有"名称"字段，将其添加到内容中
                        if row.get('名称') and content:
                            content = f"{row['名称']}：{content}"
                        
                        if category and content:
                            # Check if node already exists
                            existing_node = KnowledgeNode.query.filter_by(
                                category=category,
                                content=content
                            ).first()
                            
                            if not existing_node:
                                new_node = KnowledgeNode(
                                    category=category,
                                    content=content,
                                    source_file=filename
                                )
                                db.session.add(new_node)
                                imported_count += 1
        
        db.session.commit()
        return jsonify({'message': 'Import successful', 'imported_count': imported_count}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Import failed', 'error': str(e)}), 500

@app.route('/api/knowledge/nodes', methods=['GET'])
def get_knowledge_nodes():
    """Get all knowledge nodes"""
    category = request.args.get('category')
    if category:
        nodes = KnowledgeNode.query.filter_by(category=category).all()
    else:
        nodes = KnowledgeNode.query.all()
    
    result = []
    for node in nodes:
        result.append({
            'id': node.id,
            'category': node.category,
            'content': node.content,
            'source_file': node.source_file,
            'created_at': node.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200

@app.route('/api/knowledge/relationships', methods=['GET'])
def get_knowledge_relationships():
    """Get all knowledge relationships"""
    relationships = KnowledgeRelationship.query.all()
    result = []
    for rel in relationships:
        result.append({
            'id': rel.id,
            'source_node_id': rel.source_node_id,
            'target_node_id': rel.target_node_id,
            'relationship_type': rel.relationship_type,
            'created_at': rel.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200

@app.route('/api/knowledge/nodes', methods=['POST'])
def add_knowledge_node():
    """Add a new knowledge node"""
    data = request.get_json()
    
    if not data.get('category') or not data.get('content'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    new_node = KnowledgeNode(
        category=data['category'],
        content=data['content'],
        source_file=data.get('source_file')
    )
    
    db.session.add(new_node)
    db.session.commit()
    
    return jsonify({'message': 'Node added', 'node_id': new_node.id}), 201

@app.route('/api/knowledge/relationships', methods=['POST'])
def add_knowledge_relationship():
    """Add a new knowledge relationship"""
    data = request.get_json()
    
    if not data.get('source_node_id') or not data.get('target_node_id') or not data.get('relationship_type'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    # Check if nodes exist
    if not KnowledgeNode.query.get(data['source_node_id']) or not KnowledgeNode.query.get(data['target_node_id']):
        return jsonify({'message': 'One or both nodes do not exist'}), 404
    
    new_relationship = KnowledgeRelationship(
        source_node_id=data['source_node_id'],
        target_node_id=data['target_node_id'],
        relationship_type=data['relationship_type']
    )
    
    db.session.add(new_relationship)
    db.session.commit()
    
    return jsonify({'message': 'Relationship added', 'relationship_id': new_relationship.id}), 201

@app.route('/api/knowledge/nodes/<int:id>', methods=['DELETE'])
def delete_knowledge_node(id):
    """Delete a knowledge node"""
    node = KnowledgeNode.query.get_or_404(id)
    db.session.delete(node)
    db.session.commit()
    return jsonify({'message': 'Node deleted'}), 200

@app.route('/api/knowledge/relationships/<int:id>', methods=['DELETE'])
def delete_knowledge_relationship(id):
    """Delete a knowledge relationship"""
    relationship = KnowledgeRelationship.query.get_or_404(id)
    db.session.delete(relationship)
    db.session.commit()
    return jsonify({'message': 'Relationship deleted'}), 200

@app.route('/api/knowledge/graph', methods=['GET'])
def get_knowledge_graph():
    """Get integrated knowledge graph data for frontend"""
    try:
        # Get all relationships
        relationships = KnowledgeRelationship.query.all()
        
        # Collect all node IDs from relationships
        node_ids = set()
        for rel in relationships:
            node_ids.add(rel.source_node_id)
            node_ids.add(rel.target_node_id)
        
        # Get only nodes that are involved in relationships
        nodes = KnowledgeNode.query.filter(KnowledgeNode.id.in_(node_ids)).all()
        
        # Format nodes for frontend
        formatted_nodes = []
        node_id_map = {}
        category_color_map = {
            '基本定义': '#244d4d',
            '历史起源': '#3a6e6e',
            '文化地位': '#4f9e9e',
            '核心特色': '#64c0c0',
            '传承人与大师': '#7fd2d2',
            '保养要点': '#99e3e3',
            '工艺流程': '#244d4d',
            '操作注意事项': '#3a6e6e',
            '材料与工具': '#4f9e9e',
            '现代创新': '#64c0c0',
            '绣品种类': '#7fd2d2',
            '针法体系': '#99e3e3'
        }
        
        # Generate positions for nodes (simple grid layout)
        categories = {}
        for i, node in enumerate(nodes):
            category = node.category
            if category not in categories:
                categories[category] = []
            categories[category].append(node)
        
        # Assign positions based on category
        x_offset = 100
        y_offset = 100
        x_step = 200
        y_step = 150
        
        for category, category_nodes in categories.items():
            for j, node in enumerate(category_nodes):
                x = x_offset + (j % 3) * x_step
                y = y_offset + len(categories) * y_step
                
                # 从内容中提取名称（如果有），否则使用类别作为名称
                content = node.content
                name = node.category  # 默认使用类别作为名称
                
                # 尝试从内容中提取名称（如果内容格式为"名称：内容"）
                if ':' in content:
                    name_part = content.split(':', 1)[0].strip()
                    if name_part:
                        name = name_part
                
                formatted_node = {
                    'id': str(node.id),
                    'name': name,
                    'category': node.category,
                    'x': x,
                    'y': y,
                    'size': 30,
                    'color': category_color_map.get(category, '#244d4d')
                }
                formatted_nodes.append(formatted_node)
                node_id_map[node.id] = formatted_node
        
        # Format relationships for frontend
        formatted_links = []
        for rel in relationships:
            formatted_links.append({
                'source': str(rel.source_node_id),
                'target': str(rel.target_node_id)
            })
        
        # Find the main 湘绣 node with id 60 and set it as central node
        main_xiangxiu_node = None
        for i, node in enumerate(formatted_nodes):
            if node['id'] == '60':
                # Set this node as central
                node['x'] = 400
                node['y'] = 200
                node['size'] = 50
                node['color'] = '#244d4d'
                main_xiangxiu_node = node
                break
        
        # 不再自动添加与中心节点的连接，只保留数据库中存在的关系
        # 这样只有存在关系的节点才会连线
        
        # Create node details mapping
        node_details = {}
        for node in nodes:
            node_details[str(node.id)] = {
                'name': node.category,
                'category': node.category,
                'description': node.content,
                'related': []
            }
        
        # Add related nodes for each node
        for node in formatted_nodes:
            if str(node['id']) in node_details:
                # Find related nodes
                related_nodes = []
                for link in formatted_links:
                    if link['source'] == node['id']:
                        for n in formatted_nodes:
                            if n['id'] == link['target']:
                                related_nodes.append(n['name'])
                                break
                    elif link['target'] == node['id']:
                        for n in formatted_nodes:
                            if n['id'] == link['source']:
                                related_nodes.append(n['name'])
                                break
                node_details[str(node['id'])]['related'] = related_nodes
        
        return jsonify({
            'nodes': formatted_nodes,
            'links': formatted_links,
            'nodeDetails': node_details
        }), 200
    except Exception as e:
        return jsonify({'message': 'Error getting graph data', 'error': str(e)}), 500

# 管理页面路由
@app.route('/admin')
@admin_required
def admin_index():
    # 获取节点数量
    node_count = KnowledgeNode.query.count()
    # 获取关系数量
    relationship_count = KnowledgeRelationship.query.count()
    # 获取产品数量
    product_count = Product.query.count()
    # 获取用户数量
    user_count = User.query.count()
    # 获取最近的节点
    recent_nodes = KnowledgeNode.query.order_by(KnowledgeNode.created_at.desc()).limit(5).all()
    # 获取最近的产品
    recent_products = Product.query.order_by(Product.created_at.desc()).limit(5).all()
    
    return render_template('admin/index.html', 
                           node_count=node_count, 
                           relationship_count=relationship_count, 
                           product_count=product_count, 
                           user_count=user_count,
                           recent_nodes=recent_nodes,
                           recent_products=recent_products,
                           current_user=session)



@app.route('/admin/nodes')
@admin_required
def admin_nodes():
    # 获取搜索参数
    search_term = request.args.get('search', '')
    selected_category = request.args.get('category', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # 构建查询
    query = KnowledgeNode.query
    
    # 应用搜索过滤
    if search_term:
        query = query.filter(
            (KnowledgeNode.category.like(f'%{search_term}%')) |
            (KnowledgeNode.content.like(f'%{search_term}%'))
        )
    
    # 应用类别过滤
    if selected_category:
        query = query.filter(KnowledgeNode.category == selected_category)
    
    # 获取所有类别
    categories = [category[0] for category in db.session.query(KnowledgeNode.category).distinct().all()]
    
    # 分页
    pagination = query.order_by(KnowledgeNode.id.desc()).paginate(page=page, per_page=per_page, error_out=False)
    nodes = pagination.items
    total_nodes = pagination.total
    total_pages = pagination.pages
    
    return render_template('admin/nodes.html', 
                           nodes=nodes, 
                           search_term=search_term, 
                           selected_category=selected_category, 
                           categories=categories, 
                           page=page, 
                           total_nodes=total_nodes, 
                           total_pages=total_pages,
                           current_user=session)

@app.route('/admin/nodes/add', methods=['POST'])
@admin_required
def admin_add_node():
    # 获取表单数据
    category = request.form.get('category')
    content = request.form.get('content')
    source_file = request.form.get('source_file')
    
    # 创建新节点
    new_node = KnowledgeNode(
        category=category,
        content=content,
        source_file=source_file
    )
    
    try:
        db.session.add(new_node)
        db.session.commit()
        return jsonify({'message': 'Node added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to add node', 'error': str(e)}), 500

@app.route('/admin/nodes/edit', methods=['POST'])
@admin_required
def admin_edit_node():
    # 获取表单数据
    node_id = request.form.get('id', type=int)
    category = request.form.get('category')
    content = request.form.get('content')
    source_file = request.form.get('source_file')
    
    # 查找节点
    node = KnowledgeNode.query.get(node_id)
    if not node:
        return jsonify({'message': 'Node not found'}), 404
    
    # 更新节点
    node.category = category
    node.content = content
    node.source_file = source_file
    
    try:
        db.session.commit()
        return jsonify({'message': 'Node updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update node', 'error': str(e)}), 500

@app.route('/admin/nodes/delete/<int:id>', methods=['POST'])
@admin_required
def admin_delete_node(id):
    # 查找节点
    node = KnowledgeNode.query.get(id)
    if not node:
        return jsonify({'message': 'Node not found'}), 404
    
    try:
        db.session.delete(node)
        db.session.commit()
        return jsonify({'message': 'Node deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete node', 'error': str(e)}), 500

@app.route('/admin/products')
@admin_required
def admin_products():
    # 获取搜索参数
    search_term = request.args.get('search', '')
    category = request.args.get('category')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # 构建查询
    query = Product.query
    
    # 应用搜索过滤
    if search_term:
        query = query.filter(
            (Product.name.like(f'%{search_term}%')) |
            (Product.description.like(f'%{search_term}%'))
        )
    
    # 应用类别过滤
    if category:
        query = query.filter(Product.category == category)
    
    # 获取所有类别
    categories = [category[0] for category in db.session.query(Product.category).distinct().all()]
    
    # 分页
    pagination = query.order_by(Product.id.desc()).paginate(page=page, per_page=per_page, error_out=False)
    products = pagination.items
    total_products = pagination.total
    total_pages = pagination.pages
    
    return render_template('admin/products.html', 
                           products=products, 
                           search_term=search_term, 
                           category=category,
                           categories=categories,
                           page=page, 
                           total_products=total_products, 
                           total_pages=total_pages,
                           current_user=session)

@app.route('/admin/users')
@admin_required
def admin_users():
    # 获取搜索参数
    search_term = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # 构建查询
    query = User.query
    
    # 应用搜索过滤
    if search_term:
        query = query.filter(
            (User.username.like(f'%{search_term}%')) |
            (User.email.like(f'%{search_term}%'))
        )
    
    # 分页
    pagination = query.order_by(User.id.desc()).paginate(page=page, per_page=per_page, error_out=False)
    users = pagination.items
    total_users = pagination.total
    total_pages = pagination.pages
    
    return render_template('admin/users.html', 
                           users=users, 
                           search_term=search_term, 
                           page=page, 
                           total_users=total_users, 
                           total_pages=total_pages,
                           current_user=session)

# 产品管理相关路由
@app.route('/admin/products/add', methods=['POST'])
def admin_add_product():
    # 获取表单数据
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price', type=float)
    description = request.form.get('description')
    image = request.form.get('image')
    
    # 创建新产品
    new_product = Product(
        name=name,
        category=category,
        price=price,
        description=description,
        image=image
    )
    
    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to add product', 'error': str(e)}), 500

@app.route('/admin/products/edit', methods=['POST'])
def admin_edit_product():
    # 获取表单数据
    product_id = request.form.get('id', type=int)
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price', type=float)
    description = request.form.get('description')
    image = request.form.get('image')
    
    # 查找产品
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    # 更新产品
    product.name = name
    product.category = category
    product.price = price
    product.description = description
    product.image = image
    
    try:
        db.session.commit()
        return jsonify({'message': 'Product updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update product', 'error': str(e)}), 500

@app.route('/admin/products/delete/<int:product_id>', methods=['POST'])
def admin_delete_product(product_id):
    # 查找产品
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete product', 'error': str(e)}), 500

# 用户管理相关路由
@app.route('/admin/users/add', methods=['POST'])
def admin_add_user():
    # 获取表单数据
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    is_admin = request.form.get('is_admin') == 'on'
    
    # 创建新用户
    new_user = User(
        username=username,
        email=email,
        password=hash_password(password),
        is_admin=is_admin
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to add user', 'error': str(e)}), 500

@app.route('/admin/users/edit', methods=['POST'])
def admin_edit_user():
    # 获取表单数据
    user_id = request.form.get('id', type=int)
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    is_admin = request.form.get('is_admin') == 'on'
    
    # 查找用户
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    # 更新用户
    user.username = username
    user.email = email
    user.is_admin = is_admin
    if password:
        user.password = hash_password(password)
    
    try:
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update user', 'error': str(e)}), 500

@app.route('/admin/users/delete/<int:user_id>', methods=['POST'])
def admin_delete_user(user_id):
    # 查找用户
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete user', 'error': str(e)}), 500

# 关系管理相关路由
@app.route('/admin/relationships')
@admin_required
def admin_relationships():
    # 获取搜索参数
    search_term = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # 构建查询
    query = KnowledgeRelationship.query
    
    # 应用搜索过滤
    if search_term:
        query = query.filter(KnowledgeRelationship.relationship_type.like(f'%{search_term}%'))
    
    # 获取所有节点（用于添加关系时选择）
    nodes = KnowledgeNode.query.all()
    
    # 分页
    pagination = query.order_by(KnowledgeRelationship.id.desc()).paginate(page=page, per_page=per_page, error_out=False)
    relationships = pagination.items
    total_relationships = pagination.total
    total_pages = pagination.pages
    
    return render_template('admin/relationships.html', 
                           relationships=relationships, 
                           nodes=nodes,
                           search_term=search_term, 
                           page=page, 
                           total_relationships=total_relationships, 
                           total_pages=total_pages,
                           current_user=session)

@app.route('/admin/relationships/add', methods=['POST'])
@admin_required
def admin_add_relationship():
    # 获取表单数据
    source_node_id = request.form.get('source_node_id', type=int)
    target_node_id = request.form.get('target_node_id', type=int)
    # 关系类型默认为 'related_to'
    relationship_type = 'related_to'
    
    # 检查节点是否存在
    source_node = KnowledgeNode.query.get(source_node_id)
    target_node = KnowledgeNode.query.get(target_node_id)
    if not source_node or not target_node:
        return jsonify({'message': 'One or both nodes do not exist'}), 404
    
    # 创建新关系
    new_relationship = KnowledgeRelationship(
        source_node_id=source_node_id,
        target_node_id=target_node_id,
        relationship_type=relationship_type
    )
    
    try:
        db.session.add(new_relationship)
        db.session.commit()
        return jsonify({'message': 'Relationship added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to add relationship', 'error': str(e)}), 500

@app.route('/admin/relationships/delete/<int:id>', methods=['POST'])
@admin_required
def admin_delete_relationship(id):
    # 查找关系
    relationship = KnowledgeRelationship.query.get(id)
    if not relationship:
        return jsonify({'message': 'Relationship not found'}), 404
    
    try:
        db.session.delete(relationship)
        db.session.commit()
        return jsonify({'message': 'Relationship deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete relationship', 'error': str(e)}), 500

@app.route('/admin/import', methods=['GET', 'POST'])
def admin_import():
    import_result = None
    
    # 获取CSV文件列表
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    if request.method == 'POST':
        try:
            # 导入数据
            imported_count = 0
            
            # 处理所有CSV文件
            for filename in csv_files:
                filepath = os.path.join(data_dir, filename)
                with open(filepath, 'r', encoding='utf-8-sig') as f:
                    import csv
                    reader = csv.DictReader(f)
                    for row in reader:
                        # 处理不同格式的CSV文件
                        category = row.get('类别')
                        content = None
                        
                        # 优先使用"内容"字段，如果没有则使用"详情"字段
                        if row.get('内容'):
                            content = row['内容']
                        elif row.get('详情'):
                            content = row['详情']
                        
                        # 如果有"名称"字段，将其添加到内容中
                        if row.get('名称') and content:
                            content = f"{row['名称']}：{content}"
                        
                        if category and content:
                            # 检查是否已存在
                            existing_node = KnowledgeNode.query.filter_by(
                                category=category,
                                content=content
                            ).first()
                            
                            if not existing_node:
                                new_node = KnowledgeNode(
                                    category=category,
                                    content=content,
                                    source_file=filename
                                )
                                db.session.add(new_node)
                                imported_count += 1
            
            db.session.commit()
            import_result = {'success': True, 'imported_count': imported_count}
        except Exception as e:
            db.session.rollback()
            import_result = {'success': False, 'error': str(e)}
    
    # 模拟导入历史
    import_history = [
        {'time': '2026-02-14 11:20', 'count': 4, 'status': 'success', 'details': '导入了4条数据记录'},
        {'time': '2026-02-13 15:30', 'count': 12, 'status': 'success', 'details': '导入了12条数据记录'}
    ]
    
    return render_template('admin/import.html',
                           csv_files=csv_files,
                           import_result=import_result,
                           import_history=import_history)

# ==================== 3D模型API ====================

# 支持的3D文件格式
SUPPORTED_3D_FORMATS = ['.glb', '.gltf', '.obj', '.fbx', '.stl', '.ply', '.dae']

@app.route('/api/models', methods=['GET'])
def get_models():
    """获取3D模型列表"""
    try:
        category = request.args.get('category')
        search = request.args.get('search')

        query = Model3D.query

        if category:
            query = query.filter(Model3D.category == category)

        if search:
            query = query.filter(Model3D.name.contains(search))

        models = query.order_by(Model3D.created_at.desc()).all()

        result = []
        for model in models:
            result.append({
                'id': model.id,
                'name': model.name,
                'description': model.description,
                'file_path': model.file_path,
                'file_size': model.file_size,
                'category': model.category,
                'created_at': model.created_at.strftime('%Y-%m-%d %H:%M:%S') if model.created_at else None,
                'tags': [{'id': tag.id, 'name': tag.name} for tag in model.tags]
            })

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'message': '获取模型列表失败', 'error': str(e)}), 500

@app.route('/api/models/<int:id>', methods=['GET'])
def get_model(id):
    """获取单个3D模型详情"""
    try:
        model = Model3D.query.get_or_404(id)

        result = {
            'id': model.id,
            'name': model.name,
            'description': model.description,
            'file_path': model.file_path,
            'file_size': model.file_size,
            'category': model.category,
            'created_at': model.created_at.strftime('%Y-%m-%d %H:%M:%S') if model.created_at else None,
            'tags': [{'id': tag.id, 'name': tag.name} for tag in model.tags]
        }

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'message': '获取模型详情失败', 'error': str(e)}), 500

@app.route('/api/model-categories', methods=['GET'])
def get_model_categories():
    """获取所有3D模型分类"""
    try:
        categories = db.session.query(Model3D.category).filter(
            Model3D.category.isnot(None)
        ).distinct().all()

        return jsonify([c[0] for c in categories if c[0]]), 200
    except Exception as e:
        return jsonify({'message': '获取分类失败', 'error': str(e)}), 500

@app.route('/api/model-file/<int:id>', methods=['GET'])
def get_model_file(id):
    """获取3D模型文件"""
    try:
        model = Model3D.query.get_or_404(id)

        if not os.path.exists(model.file_path):
            return jsonify({'message': '文件不存在'}), 404

        from flask import send_file
        return send_file(model.file_path, as_attachment=False)
    except Exception as e:
        return jsonify({'message': '获取文件失败', 'error': str(e)}), 500

# 3D模型管理后台路由
@app.route('/admin/models')
@admin_required
def admin_models():
    """3D模型管理页面"""
    page = request.args.get('page', 1, type=int)
    per_page = 10
    search_term = request.args.get('search', '')
    category = request.args.get('category', '')

    query = Model3D.query

    if search_term:
        query = query.filter(
            (Model3D.name.contains(search_term)) |
            (Model3D.description.contains(search_term))
        )

    if category:
        query = query.filter(Model3D.category == category)

    pagination = query.order_by(Model3D.id.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    models = pagination.items
    total_models = pagination.total
    total_pages = pagination.pages

    categories = [c[0] for c in db.session.query(Model3D.category).distinct().all() if c[0]]

    return render_template('admin/models.html',
                           models=models,
                           search_term=search_term,
                           category=category,
                           categories=categories,
                           page=page,
                           total_models=total_models,
                           total_pages=total_pages,
                           current_user=session)

@app.route('/admin/models/add', methods=['POST'])
@admin_required
def admin_add_model():
    """添加3D模型"""
    try:
        name = request.form.get('name')
        description = request.form.get('description')
        category = request.form.get('category')
        file = request.files.get('file')

        if not name or not file:
            return jsonify({'message': '名称和文件不能为空'}), 400

        # 检查文件格式
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in SUPPORTED_3D_FORMATS:
            return jsonify({
                'message': f'不支持的文件格式。支持的格式: {", ".join(SUPPORTED_3D_FORMATS)}'
            }), 400

        # 保存文件
        upload_dir = os.path.join(os.path.dirname(__file__), 'uploads', 'models')
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, file.filename)
        file.save(file_path)

        # 获取文件大小
        file_size = os.path.getsize(file_path)

        # 创建模型记录
        new_model = Model3D(
            name=name,
            description=description,
            category=category,
            file_path=file_path,
            file_size=file_size
        )

        db.session.add(new_model)
        db.session.commit()

        return jsonify({'message': '模型添加成功', 'model_id': new_model.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '添加模型失败', 'error': str(e)}), 500

@app.route('/admin/models/delete/<int:id>', methods=['POST'])
@admin_required
def admin_delete_model(id):
    """删除3D模型"""
    try:
        model = Model3D.query.get_or_404(id)

        # 删除文件
        if os.path.exists(model.file_path):
            os.remove(model.file_path)

        db.session.delete(model)
        db.session.commit()

        return jsonify({'message': '模型删除成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '删除模型失败', 'error': str(e)}), 500

# ==================== 关键词回复管理 ====================

@app.route('/admin/keywords')
@admin_required
def admin_keywords():
    """关键词回复管理页面"""
    keywords = KeywordReply.query.order_by(KeywordReply.priority.desc()).all()
    return render_template('admin/keywords.html', keywords=keywords)

@app.route('/admin/keywords/add', methods=['POST'])
@admin_required
def admin_add_keyword():
    """添加关键词回复"""
    try:
        keyword = KeywordReply(
            keyword=request.form.get('keyword', ''),
            reply_content=request.form.get('reply_content', ''),
            category=request.form.get('category', ''),
            priority=int(request.form.get('priority', 0)),
            match_type=request.form.get('match_type', 'contains'),
            is_active=request.form.get('is_active') == 'on'
        )
        db.session.add(keyword)
        db.session.commit()
        return redirect(url_for('admin_keywords'))
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '添加失败', 'error': str(e)}), 500

@app.route('/admin/keywords/edit/<int:id>', methods=['POST'])
@admin_required
def admin_edit_keyword(id):
    """编辑关键词回复"""
    try:
        keyword = KeywordReply.query.get_or_404(id)
        keyword.keyword = request.form.get('keyword', '')
        keyword.reply_content = request.form.get('reply_content', '')
        keyword.category = request.form.get('category', '')
        keyword.priority = int(request.form.get('priority', 0))
        keyword.match_type = request.form.get('match_type', 'contains')
        keyword.is_active = request.form.get('is_active') == 'on'
        db.session.commit()
        return redirect(url_for('admin_keywords'))
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '编辑失败', 'error': str(e)}), 500

@app.route('/admin/keywords/delete/<int:id>', methods=['POST'])
@admin_required
def admin_delete_keyword(id):
    """删除关键词回复"""
    try:
        keyword = KeywordReply.query.get_or_404(id)
        db.session.delete(keyword)
        db.session.commit()
        return redirect(url_for('admin_keywords'))
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': '删除失败', 'error': str(e)}), 500

# ==================== AI对话和关键词检索API ====================

import openai

# Deepseek API配置（从环境变量读取）
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
DEEPSEEK_BASE_URL = os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com')

print(f"[DEBUG] DEEPSEEK_API_KEY 加载状态: {'已设置' if DEEPSEEK_API_KEY else '未设置'}")
if DEEPSEEK_API_KEY:
    print(f"[DEBUG] API Key 前10位: {DEEPSEEK_API_KEY[:10]}...")

if not DEEPSEEK_API_KEY:
    print("[警告] DEEPSEEK_API_KEY 环境变量未设置，AI助手功能将不可用")
    print("[提示] 请在 backend/.env 文件中设置 DEEPSEEK_API_KEY=your_api_key")

def extract_keywords(text):
    """提取查询关键词（简单分词）"""
    # 移除标点符号和停用词
    stopwords = {'的', '了', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很', '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这'}
    words = []
    for word in text.split():
        # 移除标点
        word = ''.join(c for c in word if c.isalnum() or '\u4e00' <= c <= '\u9fff')
        if word and word not in stopwords and len(word) >= 2:
            words.append(word)
    return words

def search_keyword_reply(query):
    """关键词回复匹配 - 最高优先级"""
    try:
        # 查询所有启用的关键词回复，按优先级排序
        keyword_replies = KeywordReply.query.filter_by(is_active=True).order_by(KeywordReply.priority.desc()).all()
        
        query_lower = query.lower()
        
        for kr in keyword_replies:
            keywords = [k.strip().lower() for k in kr.keyword.split(',')]
            
            for keyword in keywords:
                if not keyword:
                    continue
                    
                if kr.match_type == 'exact':
                    # 精确匹配
                    if query_lower == keyword:
                        return {
                            "content": kr.reply_content,
                            "category": kr.category or "关键词回复",
                            "matched_keyword": keyword
                        }
                elif kr.match_type == 'fuzzy':
                    # 模糊匹配（包含关系）
                    if keyword in query_lower or query_lower in keyword:
                        return {
                            "content": kr.reply_content,
                            "category": kr.category or "关键词回复",
                            "matched_keyword": keyword
                        }
                else:  # contains 默认
                    # 包含匹配
                    if keyword in query_lower:
                        return {
                            "content": kr.reply_content,
                            "category": kr.category or "关键词回复",
                            "matched_keyword": keyword
                        }
        
        return None
    except Exception as e:
        print(f"关键词回复匹配失败: {e}")
        return None

def search_knowledge_keywords(query, top_k=3):
    """关键词检索知识库"""
    try:
        keywords = extract_keywords(query)
        if not keywords:
            # 没有提取到关键词，返回最新添加的知识
            nodes = KnowledgeNode.query.order_by(KnowledgeNode.id.desc()).limit(top_k).all()
        else:
            # 构建OR条件查询
            conditions = []
            for keyword in keywords:
                conditions.append(KnowledgeNode.content.like(f'%{keyword}%'))
                conditions.append(KnowledgeNode.category.like(f'%{keyword}%'))
            
            from sqlalchemy import or_
            nodes = KnowledgeNode.query.filter(or_(*conditions)).limit(top_k).all()
        
        if nodes:
            results = []
            for node in nodes:
                results.append({
                    "content": node.content,
                    "category": node.category,
                    "relevance": 0.8  # 关键词匹配固定相似度
                })
            return results
        return None
    except Exception as e:
        print(f"关键词检索失败: {e}")
        return None

def init_vector_db():
    """初始化（纯关键词检索无需额外初始化）"""
    print("使用纯关键词检索，无需初始化向量库")
    return True

def sync_knowledge_to_vector():
    """同步（纯关键词检索无需同步）"""
    print("使用纯关键词检索，无需同步向量库")
    return True

@app.route('/api/chat', methods=['POST'])
def chat():
    """AI对话接口 - 三级检索：关键词回复 > 知识库 > Deepseek API"""
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': '消息不能为空'}), 400
    
    # 1. 第一优先级：关键词回复匹配
    keyword_reply = search_keyword_reply(user_message)
    if keyword_reply:
        return jsonify({
            'source': 'keyword_reply',
            'answer': keyword_reply['content'],
            'category': keyword_reply['category'],
            'matched_keyword': keyword_reply.get('matched_keyword', '')
        })
    
    # 2. 第二优先级：知识库关键词检索
    knowledge_results = search_knowledge_keywords(user_message, top_k=3)
    if knowledge_results:
        # 构建知识库回答
        answer_parts = []
        for i, result in enumerate(knowledge_results, 1):
            answer_parts.append(f"{i}. 【{result['category']}】{result['content']}")
        
        knowledge_answer = "\n\n".join(answer_parts)
        return jsonify({
            'source': 'knowledge_base',
            'answer': knowledge_answer,
            'references': knowledge_results
        })
    
    # 3. 第三优先级：调用Deepseek API
    if not DEEPSEEK_API_KEY:
        return jsonify({
            'error': 'AI服务未配置，请联系管理员设置 DEEPSEEK_API_KEY 环境变量'
        }), 503
    
    try:
        print(f"[DEBUG] 正在调用 Deepseek API，用户消息: {user_message[:50]}...")
        print(f"[DEBUG] API Key: {DEEPSEEK_API_KEY[:15]}...")
        print(f"[DEBUG] API URL: {DEEPSEEK_BASE_URL}")
        
        client = openai.OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是湘绣文化专家助手，回答要专业、简洁、有文化内涵。"},
                {"role": "user", "content": user_message}
            ],
            stream=False
        )
        
        ai_response = response.choices[0].message.content
        print(f"[DEBUG] Deepseek API 响应: {ai_response[:100]}...")
        
        return jsonify({
            'source': 'deepseek',
            'answer': ai_response
        })
    except openai.AuthenticationError as e:
        print(f"[错误] Deepseek API 认证失败: {str(e)}")
        return jsonify({'error': 'API 认证失败，请检查 API Key 是否正确'}), 401
    except openai.RateLimitError as e:
        print(f"[错误] Deepseek API 请求过于频繁: {str(e)}")
        return jsonify({'error': '请求过于频繁，请稍后再试'}), 429
    except Exception as e:
        print(f"[错误] Deepseek API 调用失败: {str(e)}")
        return jsonify({'error': f'AI服务暂时不可用: {str(e)}'}), 500

@app.route('/api/knowledge/import-file', methods=['POST'])
def import_knowledge_file():
    """导入Excel/CSV文件到知识库"""
    if 'file' not in request.files:
        return jsonify({'error': '未上传文件'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '文件名为空'}), 400
    
    try:
        # 根据文件扩展名选择读取方式
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file, encoding='utf-8-sig')
        elif file.filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            return jsonify({'error': '不支持的文件格式，请上传CSV或Excel文件'}), 400
        
        imported_count = 0
        for _, row in df.iterrows():
            # 支持多种列名格式
            category = row.get('category') or row.get('类别') or row.get('分类')
            content = row.get('content') or row.get('内容') or row.get('详情')
            
            if category and content:
                # 检查是否已存在
                existing = KnowledgeNode.query.filter_by(
                    category=str(category),
                    content=str(content)
                ).first()
                
                if not existing:
                    new_node = KnowledgeNode(
                        category=str(category),
                        content=str(content),
                        source_file=file.filename
                    )
                    db.session.add(new_node)
                    imported_count += 1
        
        db.session.commit()
        
        # 同步到向量库
        sync_knowledge_to_vector()
        
        return jsonify({
            'success': True,
            'message': f'成功导入 {imported_count} 条知识',
            'imported_count': imported_count
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'导入失败: {str(e)}'}), 500

@app.route('/api/knowledge/sync', methods=['POST'])
def sync_knowledge():
    """手动触发知识库同步到向量库"""
    try:
        sync_knowledge_to_vector()
        return jsonify({'success': True, 'message': '知识库同步完成'})
    except Exception as e:
        return jsonify({'error': f'同步失败: {str(e)}'}), 500

# 应用启动时初始化向量库
@app.before_request
def before_request():
    """每个请求前检查向量库是否初始化"""
    global vector_collection, embedding_model
    if vector_collection is None and VECTOR_SEARCH_AVAILABLE:
        init_vector_db()

if __name__ == '__main__':
    # 启动时初始化向量库
    with app.app_context():
        init_vector_db()
    app.run(debug=True)
