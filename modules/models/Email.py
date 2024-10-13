import smtplib
class Email:
    mail_data = {
            'login': 'testemailsendnnn1k@gmail.com',
            'password': 'znwt bffc blls fpqp',

        }

    def post_mail(self, message, user_to):
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        smt.starttls()

        smt.login(self.mail_data['login'], self.mail_data['password'])
        smt.sendmail(self.mail_data['login'], user_to, message.encode('utf-8'))
        smt.quit()
