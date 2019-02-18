# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:'ryo'
from flask import Flask
from flask import request
from xml.etree import ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'

@app.route('/ryo')
def ryo():
    return u'我是ryo'

@app.route('/weixin',method=['GET','POST'])
def weixin():
    if request.method == 'GET':
        echostr = request.args.get('echostr')
        return echostr
    data = request.get_data()
    xml = ET.fromstring(data)
    return data

if __name__ == '__main__':
    app.run(debug = True,host = '0.0.0.0',port = 2346)