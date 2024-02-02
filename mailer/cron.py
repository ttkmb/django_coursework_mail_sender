from mailer.models import Mailer
from mailer.services import process_mailer_tasks


def daily_mail():
    mailings = Mailer.objects.filter(frequency='DAY', status='LAUNCHED')
    if mailings.exists():
        process_mailer_tasks()


def weekly_mail():
    mailings = Mailer.objects.filter(frequency='WEEK', status='LAUNCHED')
    if mailings.exists():
        process_mailer_tasks()


def monthly_mail():
    mailings = Mailer.objects.filter(frequency='MONTH', status='LAUNCHED')
    if mailings.exists():
        process_mailer_tasks()
