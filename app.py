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

@app.route('/info', methods=['GET', 'POST'])
def info_page():
    return render_template('info.html')

@app.route('/services', methods=['GET', 'POST'])
def services_page():
    return render_template('services.html')

@app.route('/reviews', methods=['GET', 'POST'])
def reviews_page():
    return render_template('reviews.html')



@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('auth.login_page') + '?next=' + request.url)

    #if response.status_code == 500:
    #return redirect(url_for('error_500'))

    return response

@manager.user_loader
def load_user(user_id):
    return get_user_for_id(user_id)

if __name__ == '__main__':
    app.run()

