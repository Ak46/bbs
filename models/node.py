from . import db
from . import ReprMixin


class Node(db.Model, ReprMixin):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String())
    # content = db.Column(db.String())
    keywords = db.Column(db.String(100))
    # permit = db.Column(db.String())
    master = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, default=0)

    # blog_all = db.relationship('Blog', backref='user')
    node_blog = db.relationship('Blog', backref='node', foreign_keys='Blog.board_id')


    def __init__(self, form):
        print('node init', form)
        # self.name = form.get('name', '')
        # self.content = form.get("content", '')
        self.keywords = form.get("keywords", '板块')
        # self.master = form.get('master', '')
        self.parent_id = form.get("parent_id", 0)
        # self.permit = form.get("permit", '')

    @classmethod
    def _delete(cls, mid):
        m = cls.query.get(mid)
        print('_delte ', m)
        m.delete()

    def update(self, form):
        print('board.update, ', form)

