import smtplib
PASSWORD = 'MY_PASSWORD'
FROM = 'MY_EMAIL_ADDRESS'
TO = ['SEND_TO']
SUBJECT = 'My Subject'
TEXT = 'This is my main text'
MESSAGE = "\r\n".join(["From: "+FROM, "To: "+str(TO),
                       "Subject: "+SUBJECT, "", TEXT])
# print(MESSAGE)

class Mail:
    def __init__(self, FROM, TO, TEXT):
        self.FROM = FROM
        self.TO = TO
        self.TEXT = TEXT

    @staticmethod
    def send_mail():
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.starttls()
        mail.ehlo()
        mail.login(FROM, PASSWORD)
        mail.sendmail(FROM, TO, MESSAGE)
        mail.close()

if __name__ == '__main__':
    send_my_mail = Mail
    Mail.send_mail()
