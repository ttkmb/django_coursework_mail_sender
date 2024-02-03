from mailer.models import Mailer
from mailer.services import process_mailer_tasks


def send_mail_day_week_month():
    process_mailer_tasks()
    print('Рассылка запущена')
