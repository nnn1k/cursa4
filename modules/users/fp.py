from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from modules.database.queries.user_queries import *
from modules.database.queries.verification_code_queries import *
from modules.func.utils import get_random_code, post_mail


fp = Blueprint('fp', __name__, template_folder='templates', static_folder='static')

@fp.route('/email', methods=['GET', 'POST'])
def forgot_password_email_page():
    if request.method == 'POST':
        email = request.form.get('email')

        user = get_user_for_email(email)
        if user:
            code = get_random_code()
            message = f'''
            your code is {code}
            '''
            add_verification_code(user.id, code)
            post_mail(email, message)
            return redirect(url_for('fp.forgot_password_code_page'))
        else:
            flash('Нету пользователя с такой почтой')

    return render_template('auth/forgot_password/email.html', page_type='auth')


@fp.route('/code', methods=['GET', 'POST'])
def forgot_password_code_page():
    if request.method == 'POST':
        code = request.form.get('code')

        verification_code = get_verification_code(code)
        if verification_code:
            user = get_user_for_id(verification_code.user_id)
            login_user(user)
            return redirect(url_for('fp.new_password_page'))
        else:
            flash('Неправильный код')

    return render_template('auth/forgot_password/confirm.html', page_type='auth')

@fp.route('/new_password', methods=['GET', 'POST'])
@login_required
def new_password_page():
    if request.method == 'POST':
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if password == password2:
            user = update_password(current_user.id, password)
            drop_verification_code(user.id)
            return redirect(url_for('profile.profile_page'))

    return render_template('/auth/forgot_password/forgot_password.html', page_type='auth')
