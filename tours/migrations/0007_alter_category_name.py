# Generated by Django 3.2.7 on 2021-11-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_auto_20211127_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
