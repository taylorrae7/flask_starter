from flask import render_template, Blueprint, request
from flask_login import login_required
home_bp = Blueprint('home', __name__)


################
#### routes ####
################


@home_bp.route('/')
def home():
    return render_template('pages/home.html')


@home_bp.route('/about')
@login_required
def about():
    return render_template('pages/about.html')

