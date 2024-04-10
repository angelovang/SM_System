from django.core.mail import send_mail

from sm_system import settings


def send_email(user, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=('angelovang55@gmail.com', user.email,)
    )

    return
