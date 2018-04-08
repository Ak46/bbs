from models.user import User
from routes import *
import os


main = Blueprint('user', __name__)

Model = User


xfrs_dict = {
    'd40a58205d884331aa7f2a7304ad6345': 0,
}

def random_string():
    import uuid
    return str(uuid.uuid4())


@main.route('/')
def index():
    xfrs = random_string()
    xfrs_dict[xfrs] = 0
    log('xfrs', xfrs_dict)
    return render_template('users/login_index.html', xfrs=xfrs)


@main.route('/login', methods=['post'])
def login():
    form = request.form
    u = User(form)
    log('当前登陆的用户: ', u.username)
    if u.valid_login():
            session['username'] = u.username
            return redirect('/')
    else:
        msg = '请输入用户名或密码'
        return render_template('users/login_index.html', msgs=msg)


@main.route('/sing')
def sin_up():
    u = current_user()
    username = u.username
    session.pop(username,None)
    log('用户登出成功')
    return redirect('/')


@main.route('/register', methods=['post'])
def register():
    form = request.form
    username = User(form)
    s, m = username.valid()
    print('register ', s, m)
    if s:
        User.new(form)
        return redirect(url_for('.index'))
    else:
        return render_template('/users/login_index.html', msg=m)


@main.route('/edit/<id>')
def edit(id):
    m = Model.query.get(id)
    return render_template('/users/edit.html', user=m)


@main.route('/detail')
@login_required
def detail():
    '''
    1.用户个人信息
        返回界面
    :return:
    '''
    u = current_user()
    log('user detail 当前用户{}:{}'.format(u.id, u.username))
    return render_template('users/detail.html', user=u)


@main.route('/upload', methods=['post'])
def upload_file():
    u = current_user()
    uploads_dir = 'static/img/'
    print('upload')
    f = request.files.get('uploaded')
    if f:
        filename = f.filename
        print('filename, ', filename)
        import uuid
        ext = filename.split('.')[-1]
        valid_filetypes = ('png', 'jpg', 'jpeg', 'gif', 'apng', 'rar', 'zip')
        if ext not in valid_filetypes:
            return '不合法'
        filename = str(uuid.uuid4()) + '.' + filename.split('.')[-1]
        path = uploads_dir + filename
        # path = filename
        print(os.getcwd())
        u.file_path(path)
        f.save(path)
        return redirect(url_for('.detail'))
    else:
        return '<h1>没有上传</h1>'


