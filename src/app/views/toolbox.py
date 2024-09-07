from flask import Blueprint, render_template, request

bp = Blueprint('toolbox', __name__)


@bp.route('/toolbox')
@bp.route('/')
def index():
    return render_template("toolbox.html")

