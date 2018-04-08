from routes import *
from models.node import Node

main = Blueprint('node', __name__)

@main.route('/')
def index():
    ns = Node.query.all()
    log('node index', ns)
    return render_template('node_add.html', nodes=ns)


@main.route('/add', methods=['post'])
def add():
    form = request.form
    Node.new(form)
    return redirect(url_for('.index'))