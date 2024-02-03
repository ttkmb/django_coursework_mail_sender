from datetime import datetime
import smtplib

from django.conf import settings
from django.core.mail import send_mail
from mailer.models import MailerLogger, Mailer


def send_mail_and_log(mail_setting: Mailer, client: Mailer.clients):
    """
    Отправка письма с логированием
    """
    mail = mail_setting.mail
    status = MailerLogger.STATUS.SUCCESS
    mail_id = Mailer.objects.get(pk=mail_setting.pk)
    error_msg = None
    try:
        send_mail(
            subject=mail.title,
            message=mail.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client],
        )
    except smtplib.SMTPException as e:
        error_msg = e
        status = MailerLogger.STATUS.FAILED
    except Exception as e:
        error_msg = e
        status = MailerLogger.STATUS.FAILED
    finally:
        log = MailerLogger.objects.create(
            status=status,
            response=error_msg,
            mail=mail_id,
        )
        log.save()


def process_mail_settings(mails_settings):
    time_now = datetime.now().astimezone(None)
    for mail_setting in mails_settings:
        if mail_setting.time_start <= time_now <= mail_setting.time_stop:
            for client in mail_setting.clients.all():
                send_mail_and_log(mail_setting, client)
        if time_now >= mail_setting.time_stop:
            mail_setting.status = 'COMPLETE'
            mail_setting.save()
        mail_setting.save()


def process_mailer_tasks():
    """
    Проверка логики рассылок, изменение статуса рассылки, отправка письма
    """
    mails_settings = {
        'DAY': Mailer.objects.filter(frequency='DAY', status='LAUNCHED'),
        'WEEK': Mailer.objects.filter(frequency='WEEK', status='LAUNCHED'),
        'MONTH': Mailer.objects.filter(frequency='MONTH', status='LAUNCHED')
    }
    time_now = datetime.now().astimezone(None)
    mails = Mailer.objects.filter(status='CREATED', time_start__lte=time_now, time_stop__gte=time_now)
    for mail in mails:
        mail.status = 'LAUNCHED'
        mail.save()

    for frequency, mails in mails_settings.items():
        if mails.exists():
            process_mail_settings(mails)
            break
