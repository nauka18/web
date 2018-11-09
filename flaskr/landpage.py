import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('/index', __name__, url_prefix='/')

@bp.route('/', methods=('GET',))
@bp.route('/index', methods=('GET',))
def index():
    return render_template('landpage/index.html')

@bp.route('/aboutus', methods=('GET',))
def contacts():
    return render_template('landpage/aboutus.html')
