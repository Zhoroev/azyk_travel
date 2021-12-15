from django.db import models


class Post(models.Model):
    title = models.CharField('Название', max_length=100)
    body = models.TextField('Описание', )
    link = models.URLField('Ссылка на видео', blank=True, null=True)
    image = models.ImageField('Изображение', blank=True, null=True)
    file = models.FileField('Файл', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
