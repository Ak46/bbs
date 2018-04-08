from routes import *
from models.blog import \
    Blog, Comment
from models.node import Node


main = Blueprint('blog', __name__)


def data_time():
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    return dt



@main.route('/')
def index():
    '''
    根据用户点击的节点来显示 博客
    默认为所有
    1.得到所有的node节点
    2.根据节点返回响应的数据
    '''
    ns = Node.query.all()
    form = request.args
    bid = form.get('board_id', None)
    if bid is not None:
        # bs = Blog.query.filter_by(board_id=bid).all()
        node = Node.query.get(bid)
        log('node: ', node)
        bs = node.node_blog
        log('blog index user img:and blog:{}'.format(bs))
        return render_template('blog_index.html', nodes=ns, blog=bs)
    else:
         bs = Blog.query.all()
         return render_template('blog_index.html', blog=bs, nodes=ns)


@main.route('/detail/<int:id>')
def detail(id):
    u = current_user()
    ms = Blog.query.get(id)
    cm = ms.comments
    log('所有的评论,', cm)
    return render_template('blog_detail.html', b=ms, user=u, comment=cm)


@main.route('/new')
@login_required
def new():
    u = current_user()
    print('发表新微薄', u.id, u.username )
    # 得到所有的board_id
    bid = Node.query.all()
    print('发表新微博board_id', bid)
    return render_template('blog_new.html', user=u, board=bid)


@main.route('/add', methods=['post'])
def add():
    form = request.form
    log('blog add form.get(parent_id)', form.get('user_img', 0))
    Blog.new(form)
    return redirect(url_for('.index'))


@main.route('/delete/<int:id>')
def delete(id):
    print('delete id', id)
    Blog.delete(id)
    return redirect(url_for('.index'))


@main.route('/comment/fa', methods=['post'])
@login_required
def comment_fa():
    form = request.form
    log('comment fa', form)
    bid = form.get('blog_id', -1)
    blog = Blog.query.get(bid)
    blog.comment_len()
    Comment.new(form)
    return redirect('/detail/{}'.format(bid))