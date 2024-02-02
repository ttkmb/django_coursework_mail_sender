from django.core.management import BaseCommand

from mailer.services import process_mailer_tasks


class Command(BaseCommand):
    """
    Старт запуска рассылок из консоли
    """
    def handle(self, *args, **options):
        process_mailer_tasks()
        print('Рассылка запущена')