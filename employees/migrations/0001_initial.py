# Generated by Django 3.2.7 on 2021-12-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('mobile', models.CharField(blank=True, max_length=100, null=True, verbose_name='Мобильный телефон(1)')),
                ('mobile2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Мобильный телефон(2)')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Эл. почта')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
