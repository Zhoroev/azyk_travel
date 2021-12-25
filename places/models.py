from django.db import models


class Place(models.Model):
    class Type(models.TextChoices):
        COUNTRY = 'Country'
        REGION = 'Region'
        TOWN = 'Town'
    name = models.CharField('Название', max_length=100)
    body = models.TextField('Описанние')
    type = models.CharField('Категория', max_length=50, choices=Type.choices, )

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.name


class PlacePhoto(models.Model):
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, related_name='photos', null=True, )
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d/', null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.name