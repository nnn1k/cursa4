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