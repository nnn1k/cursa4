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
        user_id = current_user.id
        add_sport_activities(user_id, id, room_id, date, time)
        return redirect(url_for('services.services_activity_page', id=id))

    return render_template('services/services_activity.html', service=service, rooms=rooms, dates=dates, times=times)

@services.route('/subscription/<id>', methods=['GET', 'POST'])
def services_subscription_page(id):
    service = select_one_services(id)
    rooms = select_rooms_for_one_service(id)
    dates = get_date_to_month_list()
    subscriptions_types = get_subscriptions_types()
    if request.method == 'POST':
        date = request.form['date']
        subscription_type_id = request.form['subscription_type']
        user_id = current_user.id
        s_t = get_one_subscriptions_types(subscription_type_id)
        match s_t.duration:
            case 'month':
                reldelta = relativedelta(months=s_t.time_duration)
            case 'year':
                reldelta = relativedelta(years=s_t.time_duration)
            case 'week':
                reldelta = relativedelta(weeks=s_t.time_duration)
            case _:
                reldelta = relativedelta(days=s_t.time_duration)
        date_split = date.split('-')
        date_start = datetime.date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
        date_end = (date_start + reldelta)
        add_subscriptions(user_id, id, subscription_type_id, date_start.strftime('%Y-%m-%d'), date_end.strftime('%Y-%m-%d'))
        return redirect(url_for('services.services_subscription_page', id=id))
    return render_template('services/services_subscription.html', service=service, rooms=rooms, dates=dates, subscriptions_types=subscriptions_types)
