import smtplib

sender_email = 'budddytestmail123@gmail.com'
epwd = 'buddytestmail'
to = 'adnananjum12@gmail.com'
content = 'hello This is the test mail from BUDDY'


def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # transport layer security
    server.login(sender_email, epwd)
    server.sendmail(sender_email, to, content)
    server.close()


sendEmail()
