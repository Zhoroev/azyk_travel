from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Review(models.Model):
    tour = models.ForeignKey('tours.Tour', on_delete=models.CASCADE,
                             null=True, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор', )
    body = models.TextField('Описание')
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.body