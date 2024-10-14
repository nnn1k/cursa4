import string
import random
import smtplib

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
