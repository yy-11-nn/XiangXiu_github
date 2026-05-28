import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """基础配置类"""
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    # 本地开发使用 root 用户或创建专用用户
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'mysql+mysqlconnector://root:hutbhutb0000@localhost:3306/xiangxiu_culture'

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'mysql+mysqlconnector://xiangxiu_culture:hutbhutb0000@localhost:3306/xiangxiu_culture'

# 配置字典，用于根据环境选择不同的配置
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
