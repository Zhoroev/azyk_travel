# Generated by Django 3.1.3 on 2021-12-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0014_auto_20211217_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
    ]