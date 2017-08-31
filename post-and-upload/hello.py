# coding:utf-8
#! /usr/bin/python
#: Filename:hello.py

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户的名称
    return 'User %s' % username

@app.route('/sum/<int:post_id>/<int:post_id2>')
def show_post(post_id,post_id2):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    sum = post_id + post_id2
    return ' %d' % sum

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    url_for('static',filename='style.css')
    return render_template('hello.html',name=name)

@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == "test" and request.form['password'] == "test123":
            return render_template('hello.html',name=request.form['username'])
        else:
            error = 'Invaild username/password'
    return render_template('login.html',error=error)



UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/upload',methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('upload.html',filename=file.filename)
        else:
            return render_template('upload.html',error="file:\""+file.filename+"\" is not in "+_filter(str(list(ALLOWED_EXTENSIONS))))
    else:
        err = 'upload is error'
    return render_template('upload.html',error="Welcome")
def allowed_file(filename):
    "判断上传文件格式并返回判断结果(True/False)"
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def _filter(str):
    "过滤集合中的指定字符"
    dirty_stuff = ["'", "[","]"]
    for stuff in dirty_stuff:
        str = str.replace(stuff, "")
    return str

if __name__ == '__main__':
    app.debug = True
    app.run()
