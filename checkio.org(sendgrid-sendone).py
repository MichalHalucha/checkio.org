import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    from_email = Email("test@example.com")
    to_email = Email(email)
    subject = SUBJECT
    content = Content("text/plain", BODY.format(name))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
