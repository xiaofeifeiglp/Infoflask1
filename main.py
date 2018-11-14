from datetime import timedelta
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session


app = Flask(__name__)

class Config: #封装应用的配置
    DEBUG = True  # 开启调试模式
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/info10" # 数据库连接地址
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪数据库变化
    REDIS_HOST = "127.0.0.1"  # redis的ip地址
    REDIS_PORT = 6379  # redis的端口

    SESSION_TYPE = "redis"  # 设置session存储的方式 redis 性能好 可以设置过期时间
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 设置保存数据的redis操作对象
    SESSION_USE_SINGER = True  # 设置sessiond是否加密
    SECRET_KEY = 'HKyoKPTu8oC5lvRld9fbmpi5Ln6/J3CunZOuZB6Ag0MFIJigKd1OfGndaPoLMBjzvNF0qvMWXWwQg0B9osCidw=='
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  #设置session过期时间,默认就支持设置过期时间


# 从对象中加载配置
app.config.from_object(Config)
# 创建数据库对象
db = SQLAlchemy(app)
# 创建redis操作对象
sr = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 初始化Session存储
Session(app)

@app.route('/')
def index():
    session["name"] = "zs"
    return "index"

if __name__ == '__main__':
    app.run(debug=True)