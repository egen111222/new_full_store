from flask_mail import Mail,Message

mail = Mail()


def send_message(title,
                 body,
                 recipients=[]):
    msg = Message(title,
                  body=body,
                  sender="НАШ_МАГАЗИН",
                  recipients=recipients)
    mail.send(msg)
