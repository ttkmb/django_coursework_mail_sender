from django.contrib.auth import get_user_model
from django.db import models

from client.models import Client


class Mailer(models.Model):
    class FREQUENCY(models.TextChoices):
        DAY = 'DAY', 'Каждый день'
        WEEK = 'WEEK', 'Каждую неделю'
        MONTH = 'MONTH', 'Каждый месяц'

    class STATUS(models.TextChoices):
        COMPLETE = 'COMPLETE', 'Завершено'
        CREATED = 'CREATED', 'Создано'
        LAUNCHED = 'LAUNCHED', 'Запущено'

    title = models.CharField(verbose_name='Название', max_length=100)
    time_start = models.DateTimeField(verbose_name='Время начала')
    time_stop = models.DateTimeField(verbose_name='Время окончания')
    frequency = models.CharField(choices=FREQUENCY.choices, verbose_name='Периодичность', max_length=100)
    status = models.CharField(choices=STATUS.choices, verbose_name='Статус рассылки', max_length=100)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты', related_name='mailers')
    mail = models.ForeignKey(to='MailerMessage', on_delete=models.CASCADE, verbose_name='Письмо',
                             related_name='settings', null=True, blank=True)

    owner = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, verbose_name='Владелец',
                              related_name='setting',
                              default=None, null=True, blank=True)

    mail = models.ForeignKey(to='MailerMessage', on_delete=models.CASCADE, verbose_name='Письмо',
                             related_name='settings', null=True, blank=True)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['id']
        permissions = (
            ('view_mailer_list', 'Может просматривать список рассылок'),
            ('change_status', 'Может отключать рассылку'),
        )

    def __str__(self):
        return self.title

    @property
    def get_frequency(self):
        return dict(self.FREQUENCY.choices).get(self.frequency)

    @property
    def get_status(self):
        return dict(self.STATUS.choices).get(self.status)


class MailerMessage(models.Model):
    title = models.CharField(verbose_name='Тема письма', max_length=100)
    message = models.TextField(verbose_name='Сообщение')
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, verbose_name='Автор',
                               related_name='messages', null=True, blank=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['id']

    def __str__(self):
        return self.title


class MailerLogger(models.Model):
    class STATUS(models.TextChoices):
        SUCCESS = 'SUCCESS', 'Успешно'
        FAILED = 'FAILED', 'Ошибка'

    date = models.DateTimeField(verbose_name='Дата и время попытки', auto_now_add=True)
    status = models.CharField(choices=STATUS.choices, verbose_name='Статус')
    response = models.TextField(verbose_name='Ответ сервера', null=True, blank=True)
    mail = models.ForeignKey(to='Mailer', on_delete=models.CASCADE, verbose_name='Рассылка', related_name='logs',
                             null=True, default=None)

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'

    def __str__(self):
        return self.status
