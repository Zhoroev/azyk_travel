# Generated by Django 3.1.3 on 2021-12-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20211215_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='body',
            field=models.TextField(verbose_name='Описанние'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='place',
            name='type',
            field=models.CharField(choices=[('Country', 'Country'), ('Region', 'Region'), ('Town', 'Town')], max_length=50, verbose_name='Категория'),
        ),
    ]
