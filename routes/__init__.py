from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
import flask
from functools import wraps

from models.user import User

# def current_user():
#     # uid = request.cookies.get('session', '')
#     # username = session.get(uid)
#     username = session['uid']
#     # print('current user', username)
#     u = User.query.filter_by(username=username).first()
#     return u


import time

def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('log.gua.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def current_user():
    username = session.get('username', '')
    u = User.query.filter_by(username=username).first()
    return u


# 套路, 直接复制即可, 这样就可以直接用了
# 这个参数 f 实际上就是路由函数
def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        log('current user check', current_user())
        if current_user() is None:
            # 用户未登录, 重定向到登录页面
            return redirect(url_for('user.index'))
        else:
            # 用户已经登录, 扔给路由函数处理
            return f(*args, **kwargs)
    return function


