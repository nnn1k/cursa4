from flask import Flask, render_template, request, url_for, send_from_directory
from flask_login import LoginManager, current_user, login_required
from modules.database.queries.user_queries import *
from modules.users.auth import auth
from modules.users.fp import fp
from modules.users.profile import profile
from modules.func.utils import *

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'D:\projects\python\kursa4\static\img\photos')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['SECRET_KEY'] = 'secretkeyyyyyyyy'

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(fp, url_prefix='/auth/forgot_password')
app.register_blueprint(profile, url_prefix='/profile')

manager = LoginManager(app)


@app.route('/')
def start_page():
    return render_template('startpage.html')


@app.route('/closed_page', methods=['GET', 'POST'])
@login_required
def closed_page():
    print(f'current_user: {current_user.__dict__}')
    return render_template('other/closed.html')

@app.route('/test_photo', methods=['GET', 'POST'])
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
            photo.save(join(app.config['UPLOAD_FOLDER'], filename))

        return redirect(url_for('download_file', name=filename))

    return render_template('other/test_photo.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

# обработка запросов

@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('auth.login_page') + '?next=' + request.url)

    #if response.status_code == 500:
    #return redirect(url_for('error_500'))

    return response


@app.route('/error_500', methods=['GET', 'POST'])
def error_500():
    return render_template('other/error_500.html')

@manager.user_loader
def load_user(user_id):
    return get_user_for_id(user_id)

if __name__ == '__main__':
    app.run()

