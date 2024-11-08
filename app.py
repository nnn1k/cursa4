from flask import Flask, render_template, request, url_for
from flask_login import LoginManager, current_user
from modules.database.queries.user_queries import *
from modules.services.services import services
from modules.users.auth import auth
from modules.users.fp import fp
from modules.users.profile import profile
from modules.func.utils import *
from modules.database.queries.review_queries import *
from modules.database.queries.services_queries import *

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'D:\projects\python\kursa4\static\img\photos')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['SECRET_KEY'] = 'secretkeyyyyyyyy'

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(fp, url_prefix='/auth/forgot_password')
app.register_blueprint(profile, url_prefix='/profile')
app.register_blueprint(services, url_prefix='/services')

manager = LoginManager(app)

@app.route('/')
def start_page():
    return render_template('startpages/startpage.html')

@app.route('/info', methods=['GET', 'POST'])
def info_page():
    if current_user.is_authenticated:
        current_user_review = get_review_for_user_id(current_user.id)
    else:
        current_user_review = None
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        submit = request.form.get('submit-review')

        match submit:
            case 'Удалить отзыв':
                delete_review_for_user_id(current_user.id)
            case 'Оставить отзыв':
                add_review(title, description, current_user.id)
            case 'Изменить отзыв':
                update_review_for_user_id(title, description, current_user.id)

        return redirect(url_for('info_page'))
    
    reviews = get_reviews()

    for review in reviews:
        review.create_at = review.create_at.strftime("%Y-%m-%d %H:%M:%S")

    return render_template('startpages/info.html', reviews=reviews, current_user_review=current_user_review)

@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('auth.login_page') + '?next=' + request.url)

    #if response.status_code == 500:
    #return redirect(url_for('test.error_500'))


    return response

@manager.user_loader
def load_user(user_id):
    return get_user_for_id(user_id)

if __name__ == '__main__':
    app.run()

