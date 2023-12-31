from flask import render_template, Blueprint, session, redirect, url_for, flash

from .main import NameForm

routes = Blueprint('routes', __name__)


@routes.route('/', methods=["GET", "POST"])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash("Looks like you changed your name")
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("routes.index"))
    return render_template('index.html', form=form, name=session.get("name"))


@routes.route('/user/')
@routes.route('/user/<name>')
def user(name=None):
    return render_template('user.html', name=name)
