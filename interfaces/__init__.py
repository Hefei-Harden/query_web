# -*- coding: utf-8 -*-
'''
    @读取数据文件
    @January, 1, 13
    @author: lc
'''

from flask_restplus import Api
from interfaces.query_inter import api as ns_keyword

api = Api(
    title='他山零件库查询系统接口',
    version='1.0'
)

api.add_namespace(ns_keyword)