from flask import render_template, request, redirect, url_for, flash, Blueprint, current_app
from flask_login import login_user, logout_user, current_user, login_required
from modules.database.queries.user_queries import *
from modules.func.utils import *
from modules.database.queries.services_queries import *

services = Blueprint('services', __name__, template_folder='templates', static_folder='static')

@services.route('/', methods=['GET', 'POST'])
def services_page():
    services = select_all_services()
    return render_template('/services/services.html', services=services)

@services.route('/activity/<id>', methods=['GET', 'POST'])
@login_required
def services_activity_page(id):
    service = select_one_services(id)
    rooms = select_rooms_for_one_service(id)
    dates = get_date_to_month_list()
    times = get_time_list()
    if request.method == 'POST':
        room_id = request.form['room']
        date = request.form['date']
        time = request.form['time']
        # привести дату и время в sql type
        print(room_id, date, time)
        print(type(room_id), type(date), type(time))
        user_id = current_user.id
        add_sport_activities(user_id, id, room_id, date, time)
        return redirect(url_for('services.services_activity_page', id=id))

    return render_template('services/services_activity.html', service=service, rooms=rooms, dates=dates, times=times)

@services.route('/subscription/<id>', methods=['GET', 'POST'])
def services_subscription_page(id):
    service = select_one_services(id)
    return render_template('services/services_subscription.html', service=service)
