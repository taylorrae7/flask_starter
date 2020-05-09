from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for, flash, Markup
from flask_login import login_user, current_user, logout_user, login_required

from app import db
from app.models import User
from app.forms.auth import LoginForm, RegisterForm


auth_bp = Blueprint('auth', __name__)


################
#### routes ####
################


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user is None:
            user = User(first_name=form.firstname.data,
                        last_name=form.lastname.data,
                        email=form.email.data,
                        password=form.password.data)

            user.registered_on = datetime.now()
            db.session.add(user)
            db.session.commit()

            message = Markup("<strong>Success!</strong> Thanks for registering")
            flash(message, 'success')
            return redirect(url_for('auth.login'))

        else:
            message = Markup("<strong>Email already registered!</strong> Please use a different email.")
            flash(message, 'danger')

    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                flash(err, 'danger')

    return render_template('pages/register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.is_correct_password(form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('home.home'))
            else:
                message = Markup("<strong>Error!</strong> Incorrect login credentials.")
                flash(message, 'danger')
        else:
            for fieldName, errorMessages in form.errors.items():
                for err in errorMessages:
                    flash(err, 'danger')

    return render_template('pages/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    """ logs out user """

    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    message = Markup("<strong>Goodbye!</strong> You are now logged out.")
    flash(message, 'info')
    return redirect(url_for('auth.login'))