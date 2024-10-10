from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from modules.database.queries.user_queries import *
from modules.users.auth.auth import auth
app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')

manager = LoginManager(app)

app.secret_key = 'secretkeyyyyyyyy'


@app.route('/')
def hello_world():
    return render_template('startpage.html')

@app.route('/closed_page', methods=['GET', 'POST'])
@login_required
def closed_page():
    print(f'current_user: {current_user.__dict__}')
    return render_template('closed.html')

@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('auth.login_page') + '?next=' + request.url)

    return response

@manager.user_loader
def load_user(user_id):
    return get_user_for_id(user_id)

if __name__ == '__main__':
    app.run()

