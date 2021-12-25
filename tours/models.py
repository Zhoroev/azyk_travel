from django.db import models
from django.db.models import Max, Count
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO: название туров в модели отзывов def __str__
# TODO: DataPrice -> OneToOneField


class Category(models.Model):
    name = models.CharField('Название', max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tour(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tours', verbose_name='Категория')
    name = models.CharField('Название', max_length=128, blank=True, null=True,)
    body = models.TextField('Описание', blank=True, null=True,)
    body_list = models.CharField('Краткое описание', max_length=250, blank=True, null=True,)
    included = models.TextField('Включено', blank=True, null=True, )
    excluded = models.TextField('Не включено', blank=True, null=True, )
    draft = models.BooleanField('Черновик', default=True, )
    image = models.ImageField('Основное изображение', upload_to='tour_pictures/%Y/%m/%d/', blank=True, null=True,)
    is_top = models.BooleanField('Топ', default=False)

    def day(self):
        days = self.programs.all().aggregate(Max('day'))
        print(days)
        if days['day__max']:
            return days['day__max']
        return 1

    def count_review(self):
        reviews = self.reviews.all()
        if reviews:
            return len(reviews)
        return 0

    day.short_description = 'Количество дней'
    count_review.short_description = 'Количество отзывов'

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='accommodation', null=True, verbose_name='Тур')
    location = models.CharField('Название места', max_length=128)
    night = models.PositiveIntegerField('Количество ночей')
    body = models.TextField('Описание')

    class Meta:
        verbose_name = 'Жилье'
        verbose_name_plural = 'Жилья'

    def __str__(self):
        return self.location


class TourPhoto(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, related_name='photos', null=True, verbose_name='Тур')
    name = models.CharField('Название', max_length=128)
    image = models.ImageField('Ссылка', upload_to='tour_pictures/%Y/%m/%d/', null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.name


class Program(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, related_name='programs', null=True, verbose_name='Тур')
    name = models.CharField('Название', max_length=128)
    body = models.TextField('Описание',)
    day = models.PositiveIntegerField('День')
    placement = models.TextField('Размещение')
    nutrition = models.TextField('Питание')

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'

    def __str__(self):
        return self.name


class DatePrice(models.Model):
    class TourStatus(models.TextChoices):
        SOLD_OUT = 'Sold out'
        COMPLETED = 'Completed'
        AVAILABLE = 'Available'
        GUARANTEED = 'Guaranteed'

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='date_prices', verbose_name='Тур')
    start = models.DateTimeField('Начало', blank=True, null=True)
    end = models.DateTimeField('Конец', blank=True, null=True)
    min_people = models.PositiveIntegerField('Минимальное количество людей',)
    max_people = models.PositiveIntegerField('Максимальное количество людей',)
    status = models.CharField('Cтатус', max_length=50, choices=TourStatus.choices, default=TourStatus.AVAILABLE)
    price = models.DecimalField('Цена', max_digits=15, decimal_places=2)

    class Meta:
        verbose_name = 'Дата и цена'
        verbose_name_plural = 'Даты и цены'

    def __str__(self):
        return self.tour.name


class Question(models.Model):
    title = models.CharField('Вопрос', max_length=100)
    body = models.TextField('Ответ', )
    image = models.ImageField(blank=True, null=True)
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, related_name='questions', null=True, blank=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title