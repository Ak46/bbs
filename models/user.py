import os

from . import ReprMixin
from . import db


class User(db.Model, ReprMixin):
    # 类的属性就是数据库表的字段
    # 这些都是内置的 __tablename__ 是表名
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    img_src = db.Column(db.String())
    # qq = db.Column(db.String())
    # email = db.Column(db.String())
    # signature = db.Column(db.String())
    #
    # credit = db.Column(db.Integer, default=100)
    # created_time = db.Column(db.Integer)
    # #
    blog_all = db.relationship('Blog', backref='user')
    # topics = db.relationship('Topic', backref='user')
    # comments = db.relationship('Comment', backref='user'.  foreign_keys='Blog.user_id')

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        # self.email = form.get('email', '')
        # self.signature = form.get('signature', '')
        # self.qq = form.get('qq', '')

    def file_path(self, f):
        self.img_src = f
        self.save()

    def valid_login(self):
        u = User.query.filter_by(username=self.username).first()
        if u is not None and u.password == self.password:
            return True
        else:
            return False
        # login_user = u
        # login_password = u.password == self.password
        #
        # msgs = []
        # if not login_user:
        #     message = '请输入用户名或注册账号'
        #     msgs.append(message)
        # if not login_password:
        #     message = '密码错误'
        #     msgs.append(message)



    def valid_username(self, username):
        return User.query.filter_by(username=self.username).first() == None

    def valid(self):
        print('valid  username', self.username)
        valid_username = self.valid_username(self.username)
        valid_username_len = len(self.username) >= 3
        valid_password_len = len(self.password) >= 3
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        if not valid_username_len:
            message = '用户名长度必须大于等于 3'
            msgs.append(message)
        if not valid_password_len:
            message = '密码长度必须大于等于 3'
            msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        print('valid end', status)
        return status, msgs

