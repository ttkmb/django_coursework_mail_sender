from django.contrib.auth import get_user_model
from django.db import models


class Client(models.Model):
    email = models.EmailField(verbose_name='Email', unique=True, max_length=100)
    fullname = models.CharField(verbose_name='ФИО', max_length=100)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, verbose_name='Владелец',
                              related_name='client',
                              default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['id']
        permissions = (
            ('view_client_list', 'Может просматривать список клиентов'),
        )

    def __str__(self):
        return self.email
