import string
import random
import smtplib
from flask import current_app, redirect, flash
from os.path import join, dirname, realpath
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

def get_random_code():
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return res

def post_mail(user_to, message):
    mail_data = {
        'login': 'testemailsendnnn1k@gmail.com',
        'password': 'znwt bffc blls fpqp',
    }
    smt = smtplib.SMTP('smtp.gmail.com', 587)
    smt.starttls()
    smt.login(mail_data['login'], mail_data['password'])
    smt.sendmail(mail_data['login'], user_to, message.encode('utf-8'))
    smt.quit()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def add_photo(request, user):
    if 'photo' not in request.files:
        flash('Не могу прочитать файл')
        return redirect(request.url)
    photo = request.files.get('photo')
    if photo.filename == '':
        if not user.photo_url:
            return 'default.png'
        return user.photo_url
    if photo:
        filename = f"{user.login}.{photo.filename.rsplit('.', 1)[1]}"
        photo.save(join(current_app.config['UPLOAD_FOLDER'], filename))
        return filename

def create_cls_object(res, cls):
    if res:
        return cls(*res)
    else:
        return None

def get_date_to_month_list():
    date1 = datetime.datetime.today() + relativedelta(days=1)
    date2 = datetime.datetime.today() + relativedelta(months=1)
    mydates = pd.date_range(date1, date2).tolist()
    return [i.strftime('%Y-%m-%d') for i in mydates]

def get_time_list():
    mytimes = []
    for i in range(9, 22):
        mytimes.append(f'{i}:00')
        mytimes.append(f'{i}:30')
    return mytimes

