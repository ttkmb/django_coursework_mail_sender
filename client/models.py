from django.db import models


# Create your models here.

class Client(models.Model):
    email = models.EmailField(verbose_name='Email', unique=True, max_length=100)
    fullname = models.CharField(verbose_name='ФИО', max_length=100)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['id']

    def __str__(self):
        return self.email
