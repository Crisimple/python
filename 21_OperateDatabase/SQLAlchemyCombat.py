#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SQLAlchemyCombat.py
@Time    :   2019/11/4 20:16
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   1.form SQLAlchemy import News, engine
             2.News.metadata.create_all(engine)
             注意： sqlchemy对于Python3不友好， 链接数据库时需要用mysql+pymysql
"""

from sqlalchemy import create_engine
from pymysql import install_as_MySQLdb
# 基类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

engine = create_engine("mysql+pymysql://root:Root@159357@129.28.170.125/PythonDatabases")
Base = declarative_base()


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300), )
    author = Column(String(20), )
    view_count = Column(Integer)
    create_at = Column(DateTime)
    is_valid = Column(Boolean)
