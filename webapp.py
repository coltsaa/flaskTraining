# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:'EiJi'
from flask import Flask
from flask import render_template #模板渲染
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'name':u'上传文件' #ascii编码 u
    }
    return render_template('index.html', **context)

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return u'请先选择文件再上传'
    file.save('static/%s' %file.filename)
    return 'http://127.0.0.1:5000/static/%s' %file.filename

if __name__ == '__main__':
    app.run(debug = True)

