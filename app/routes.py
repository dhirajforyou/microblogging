from flask import Blueprint

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return "Hello, world!"


@routes.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name}</h1>"