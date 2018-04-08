from . import db
from . import ReprMixin
from . import utctime, data_time
'''
1. blog 数据
    id
    title
    content
    create_time
    author
    views
    1.1 发表创建一个博客 new()
    1.2 增加 浏览数 views

2. comment
    id 
    content
    username
    create_time
    blog_id
    
'''
class Blog(db.Model, ReprMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(2000))
    create_time = db.Column(db.Integer, default=data_time())
    author = db.Column(db.Text)
    views = db.Column(db.Integer, default=0)
    len_comment = db.Column(db.Integer, default=0)
    user_img = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    board_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))

    comments = db.relationship('Comment', backref='blog', foreign_keys='Comment.blog_id')


    def comment_len(self):
        comment_all = self.comments
        l = len(comment_all)
        # print('评论长度是, ', l)
        self.len_comment = l + 1
        self.save()


    def __init__(self, form):
        print('blog init', form)
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.author = form.get('author', '')
        # self.len_comment = form.get('len_comment', 0)
        self.user_id = int(form.get('user_id', -1))
        self.board_id = int(form.get('parent_id', -1))
        self.user_img = form.get('user_img', '')


class Comment(db.Model, ReprMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    comment = db.Column(db.String(1000))
    create_time = db.Column(db.Integer, default=data_time())

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.username = form.get('username', '')
        self.comment = form.get('comment', '')
        self.user_id = form.get('user_id', -1)
        self.blog_id = form.get('blog_id', -1)
        self.create_time = data_time()

