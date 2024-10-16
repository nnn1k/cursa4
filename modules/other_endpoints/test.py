from flask import render_template, request, redirect, url_for, flash, Blueprint, current_app, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from modules.database.queries.user_queries import *
from modules.func.utils import *

test = Blueprint('test', __name__)

@test.route('/closed_page', methods=['GET', 'POST'])
@login_required
def closed_page():
    print(f'current_user: {current_user.__dict__}')
    return render_template('other/closed.html')

@test.route('/test_photo', methods=['GET', 'POST'])
def test_photo():
    if request.method == 'POST':
        if 'photo' not in request.files:
            flash('Не могу прочитать файл')
            return redirect(request.url)
        photo = request.files.get('photo')
        if photo.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if photo:
            type = photo.filename.rsplit('.', 1)[1]
            filename = f'test.{type}'
            photo.save(join(current_app .config['UPLOAD_FOLDER'], filename))

        return redirect(url_for('download_file', name=filename))

    return render_template('other/test_photo.html')

@test.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], name)

@test.route('/error_500', methods=['GET', 'POST'])
def error_500():
    return render_template('other/error_500.html')
