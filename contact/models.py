from django.db import models
from django.core.validators import RegexValidator


class Message(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.email


class Contact(models.Model):
    email = models.EmailField('Почта', )
    address = models.CharField('Aдрес', max_length=128)
    address_link = models.URLField('Ссылка на адрес', blank=True, null=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Phone(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phone_numbers', )

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    def __str__(self):
        return self.phone_number


class SocialMedia(models.Model):
    class Name(models.TextChoices):
        FACEBOOK = 'Facebook'
        INSTAGRAM = 'Instagram'
        SKYPE = 'Skype'
        TWITTER = 'Twitter'
        TIKTOK = 'TikTok'
        TELEGRAM = 'Telegram'
        WHATSAPP = 'WhatsApp'
        YOUTUBE = 'YouTube'

    name = models.CharField(max_length=50, choices=Name.choices, unique=True)
    link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Соц. сеть'
        verbose_name_plural = 'Соц. сети'

    def __str__(self):
        return self.name
