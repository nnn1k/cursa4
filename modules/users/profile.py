from flask import render_template, request, redirect, url_for, flash, Blueprint, current_app
from flask_login import login_user, logout_user, current_user, login_required
from modules.database.queries.user_queries import *
from modules.func.utils import *
from modules.database.queries.services_queries import get_sport_activities, get_subscriptions_history

profile = Blueprint('profile', __name__)

@profile.route('/userform', methods=['GET', 'POST'])
@login_required
def userform_page():
    user_id = current_user.id
    user = get_user_for_id(current_user.id)

    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        filename = add_photo(request, user)
        if type(filename) != str:
            return filename
        filling_form(user_id, name, surname, email, phone, filename)
        return redirect(url_for('profile.profile_page'))
    return render_template('profile/userform.html', page_type='auth', user=user)


@profile.route('/', methods=['GET', 'POST'])
@login_required
def profile_page():
    sports_activities = get_sport_activities(current_user.id)
    subscriptions = get_subscriptions_history(current_user.id)
    for subscription in subscriptions:
        date_split = subscription.date_end.split('-')
        date = datetime.datetime.now().date()
        end_date = datetime.date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
        diff_date = (end_date - date).total_seconds()
        if diff_date > 0:
            subscription.is_active = True

    return render_template('profile/lk.html', page_type='profile',
                           sports_activities=sports_activities, subscriptions=subscriptions)
