# Generated by Django 3.2.7 on 2021-11-27 15:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=128)),
                ('address_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Skype', 'Skype'), ('Twitter', 'Twitter'), ('TikTok', 'Tiktok'), ('Telegram', 'Telegram'), ('WhatsApp', 'Whatsapp'), ('YouTube', 'Youtube')], max_length=50, unique=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='contact.contact')),
            ],
        ),
    ]