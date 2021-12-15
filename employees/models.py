from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='ФИО')
    image = models.ImageField('Фотография', blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True, verbose_name='Мобильный телефон(1)')
    mobile2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Мобильный телефон(2)')
    email = models.EmailField(blank=True, null=True, verbose_name='Эл. почта')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name


