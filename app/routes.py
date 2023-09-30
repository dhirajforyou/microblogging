from flask import render_template, Blueprint

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return render_template('base.html')


@routes.route('/user/')
@routes.route('/user/<name>')
def user(name=None):
    return render_template('user.html', name=name)