# Generated by Django 3.2.7 on 2021-11-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='country',
        ),
        migrations.AlterField(
            model_name='tourphoto',
            name='image',
            field=models.ImageField(null=True, upload_to='tour_pictures/%Y/%m/%d/'),
        ),
    ]
