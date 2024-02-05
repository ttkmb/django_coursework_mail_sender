from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, verbose_name='URL')
    content = models.TextField(null=True, blank=True, verbose_name='Содержание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/blog/%Y/%m/%d/', null=True, blank=True, default=None,
                              verbose_name='Фото')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    author = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, verbose_name='Автор', default=None,
                               null=True, blank=True, related_name='post')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create']

    def __str__(self):
        return self.title

