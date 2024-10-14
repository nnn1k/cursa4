from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from modules.database.queries.user_queries import *

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if current_user.is_authenticated:
        return redirect(url_for('closed_page'))

    if request.method == 'POST':
        if not (login and password):
            flash('Заполните все поля')

        else:
            user = auth_user(login, password)

            if user:
                login_user(user)
                next_page = request.args.get('next') or url_for('hello_world')

                return redirect(next_page)

            else:
                flash('Логин или пароль не являются правильными')

    return render_template('auth/login.html', page_type='auth')


@auth.route('/register', methods=['GET', 'POST'])
def register_page():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':

        if not (login and password and password2):
            flash('Заполните все поля')

        elif password != password2:
            flash('Пароли не совпадают')
        else:
            user = get_user_for_login(login)
            if not user:
                add_user(login, password)
                login_user(get_user_for_login(login))
                return redirect(url_for('auth.userform_page'))
            else:
                flash('Пользователь уже существует')

    return render_template('auth/register.html', page_type='auth')

@auth.route('/userform', methods=['GET', 'POST'])
@login_required
def userform_page():
    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    user_id = current_user.id
    user = get_user_for_id(current_user.id)

    if request.method == 'POST':
        if not (name and surname and email and phone):
            flash('Заполните все поля')

        filling_form(user_id, name, surname, email, phone)
        return redirect(url_for('closed_page'))
    return render_template('auth/userform.html', page_type='auth', user=user)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('start_page'))

