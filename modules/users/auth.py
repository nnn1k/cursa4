from flask import render_template, request, redirect, url_for, flash, Blueprint, current_app
from flask_login import login_user, logout_user, current_user, login_required
from modules.database.queries.user_queries import *
from modules.func.utils import *

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('closed_page'))

    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if not (login and password):
            flash('Заполните все поля')
        else:
            user = auth_user(login, password)
            if user:
                login_user(user)
                next_page = request.args.get('next') or url_for('start_page')
                return redirect(next_page)
            else:
                flash('Логин или пароль не являются правильными')

    return render_template('auth/login.html', page_type='auth')


@auth.route('/register', methods=['GET', 'POST'])
def register_page():

    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not (login and password and password2):
            flash('Заполните все поля')
        elif password != password2:
            flash('Пароли не совпадают')
        else:
            user = get_user_for_login(login)
            if not user:
                add_user(login, password)
                login_user(get_user_for_login(login))
                return redirect(url_for('profile.userform_page'))
            else:
                flash('Пользователь уже существует')

    return render_template('auth/register.html', page_type='auth')

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('start_page'))

