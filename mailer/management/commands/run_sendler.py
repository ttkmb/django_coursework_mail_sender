from django.core.management import BaseCommand

from mailer.cron import daily_mail


class Command(BaseCommand):
    help = 'Запуск кронтаба с рассылками'

    def handle(self, *args, **options):
        daily_mail()
        print('Ежедневная рассылка запущена')