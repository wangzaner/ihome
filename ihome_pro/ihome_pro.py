#coding=utf-8

# 创建app对象
from manager import create_app
from config import DevelopConfig
app = create_app(DevelopConfig)

# 初始化数据
from models import db
db.init_app(app)

# 创建管理对象
from flask_script import Manager
manager = Manager(app)

# 创建迁移
from flask_migrate import Migrate, MigrateCommand
Migrate(db, app)
manager.add_command('db', MigrateCommand)

# 注册蓝图
from html_views import html_blueprint
app.register_blueprint(html_blueprint)

from api_v1.house_views import house_blueprint
app.register_blueprint(house_blueprint, url_prefix='/api/v1/house')

from api_v1.order_views import order_blueprint
app.register_blueprint(order_blueprint, url_prefix='/api/v1/order')

from api_v1.user_views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix='/api/v1/user')

from ytx_views import ytx_blueprint
app.register_blueprint(ytx_blueprint, url_prefix='/ytx')

if __name__ == '__main__':
    manager.run()













