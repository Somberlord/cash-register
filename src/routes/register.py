from flask import Blueprint, render_template
from flask_login import login_required

register = Blueprint('register', __name__)


@register.route('/register/main')
@login_required
def register_main():
    return render_template('register_main.html')
