# -*- coding: utf-8 -*-
'''
    @读取数据文件
    @January, 1, 8
    @author: lc
'''
from flask import Flask,render_template
from flask_cors import CORS
from interfaces import api


app = Flask(__name__)
CORS(app,supports_credentials=True)

api.init_app(app)
@app.route('/index/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/query/',methods=['GET','POST'])
def query():
    return render_template('query.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/404/')
def err_404():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(port=7000,debug=True)