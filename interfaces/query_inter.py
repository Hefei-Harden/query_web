# -*- coding: utf-8 -*-
'''
    @读取数据文件
    @January, 1, 13
    @author: lc
'''
from flask import Flask
from flask import request,make_response,render_template
from flask_restplus import Resource,Namespace
from common import creatDBS
from common.config import Code_dict
import json

api = Namespace('Keywords',description='根据关键词查询')

#关键词查询接口
@api.route('/KeywordsQUERY',methods=['GET','POST'])
@api.param('key_words','请输入您要搜索的关键字',_in='formData',type='str')
#@api.param('table_name','需要查询的零件类型',_in='formData',type='str')

class key_words_all(Resource):
    def post(self):
        try:
            result_dict = {}
            key_words = request.values.get('key_words')
            result = creatDBS.key_word_query_all(key_words)
            #result = render_template("query2.html",name='key_words',result_dict=result)
            if len(result)>0:
                result_dict['code'] = 1
                result_dict['value'] = result
            else:
                result_dict['code'] = 0
                result_dict['value'] = None
            response = make_response(result)
            response.headers['Content-Type'] = 'json'
            return response
        except Exception as ex:
            print("出现如下异常：%s" % ex)

    def get(self):
        try:
            key_words = request.values.get('key_words')
            result_dict = {}
            result = creatDBS.key_word_query_all(key_words)
            #result = render_template("query2.html",name='key_words',result_dict=result)
            if len(result)>0:
                result_dict['code'] = 1
            else:
                result_dict['code'] = 0
                result_dict['value'] = None
            result_dict.update(result)
            response = make_response(result_dict)
            response.headers['Content-Type'] = 'json'
            return response
        except Exception as ex:
            print("出现如下异常：%s" % ex)

#登陆接口
@api.route('/login_in', methods=['GET','POST'])
@api.param('username','用户名',_in='formData',type='str')
@api.param('password','密码',_in='formData',type='str')
class Login_Form(Resource):
    def post(self):
        try:
            username = request.values.get('username')
            password = request.values.get('password')
            result,re_str = creatDBS.Is_login_in(username,password)

            response = make_response(result)
            response.headers['Content-Type'] = 'json'
            return response
        except Exception as ex:
            print("出现如下异常：%s" % ex)

    def get(self):
        try:
            username = request.values.get('username')
            password = request.values.get('password')
            result_dict={}
            result,re_str = creatDBS.Is_login_in(username,password)
            result_dict['code'] = result
            result_dict['msg'] = re_str
            #result = render_template("login2.html", msg=re_str)
            response = make_response(result_dict)
            response.headers['Content-Type'] = 'json'
            return response
        except Exception as ex:
            print("出现如下异常：%s" % ex)

#限定表
@api.route('/table_query', methods=['GET','POST'])
@api.param('key_words','请输入您要搜索的关键字',_in='formData',type='str')
@api.param('table_name','需要查询的零件类型',_in='formData',type='str')
class query_table(Resource):
    def post(self):
        try:
            result_dict = {}
            key_words = request.values.get('key_words')
            table_name = request.values.get('table_name')
            #table_name_z = request.values.get('table_name_z')
            if key_words == '编码汇总':
                result = creatDBS.key_word_query_BMHZ(key_words,key_words,'')
            elif len(table_name) < 1 or table_name=='全部':
                result = creatDBS.key_word_query_all(key_words)
            else:
                result = creatDBS.key_word_query_table(table_name, key_words)
            if len(result) > 0:
                result_dict['code'] = 1
                result_dict['value'] = result
            else:
                result_dict['code'] = 0
                result_dict['value'] = None
            response = make_response(result_dict)
            response.headers['Content-Type'] = 'json'
            return response
        except Exception as ex:
            print("出现如下异常：%s" % ex)

    def get(self):
        try:
            result_dict = {}
            key_words = request.values.get('key_words')
            table_name = request.values.get('table_name')
            # table_name_z = request.values.get('table_name_z')
            result = creatDBS.key_word_query_table(table_name, key_words)
            if len(result) > 0:
                result_dict['code'] = 1
                result_dict['value'] = result
            else:
                result_dict['code'] = 0
                result_dict['value'] = None
            response = make_response(result_dict)
            response.headers['Content-Type'] = 'json'
            return response
        except Exception as ex:
            print("出现如下异常：%s" % ex)