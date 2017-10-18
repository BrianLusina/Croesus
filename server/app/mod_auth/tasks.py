from app import celery, mail
from flask_mail import Message
from flask import current_app, render_template


def send_email(to, subject, template):
    """
    Sends a confirmation email to registering user
    :param to: who we are sending this email to
    :param subject: subject of email
    :param template: template of the email
    """
    msg = Message(
        subject=subject,
        recipients=[to],
        html=template,
        sender=current_app.config.get("MAIL_DEFAULT_SENDER")
    )
    mail.send(msg)


@celery.task
def send_mail_async(to, subject, template, confirm_url):
    """
    Task to send mail asynchronously
    :param confirm_url: Url used to confirm user email
    :param template: template to use in the email sent
    :param subject: subject of email
    :param to: recipients of this email
    """
    app = current_app._get_current_object()

    msg = Message(
        subject=app.config["MAIL_SUBJECT_PREFIX"] + " " + subject,
        sender=app.config.get("MAIL_DEFAULT_SENDER"),
        recipients=[to],
    )
    msg.html = render_template(template, confirm_url=confirm_url)

    with current_app.app_context():
        mail.send(msg)
