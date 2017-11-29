#coding=utf-8
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class BaseModel(object):
    create_time = db.Column(db.DATETIME, default=datetime.now)
    update_time = db.Column(db.DATETIME, default=datetime.now, onupdate=datetime.now)