# Generated by Django 3.1.3 on 2021-12-15 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20211209_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name': 'Номер телефона', 'verbose_name_plural': 'Номера телефонов'},
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'Соц. сеть', 'verbose_name_plural': 'Соц. сети'},
        ),
    ]
