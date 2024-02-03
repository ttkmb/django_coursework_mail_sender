from django.core.management import BaseCommand

from mailer.cron import send_mail_day_week_month


class Command(BaseCommand):
    help = 'Запуск кронтаба с рассылками'

    def handle(self, *args, **options):
        send_mail_day_week_month()