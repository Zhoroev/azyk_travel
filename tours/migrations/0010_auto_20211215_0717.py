# Generated by Django 3.1.3 on 2021-12-15 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_auto_20211209_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accommodation',
            options={'verbose_name': 'Жилье', 'verbose_name_plural': 'Жилья'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='dateprice',
            options={'verbose_name': 'Дата и цена', 'verbose_name_plural': 'Даты и цены'},
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'verbose_name': 'Программа', 'verbose_name_plural': 'Программы'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': 'Тур', 'verbose_name_plural': 'Туры'},
        ),
        migrations.AlterModelOptions(
            name='tourphoto',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='body',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='location',
            field=models.CharField(max_length=128, verbose_name='Название места'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='night',
            field=models.PositiveIntegerField(verbose_name='Количество ночей'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accommodation', to='tours.tour', verbose_name='Тур'),
        ),
        migrations.AlterField(
            model_name='dateprice',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='dateprice',
            name='max_people',
            field=models.PositiveIntegerField(verbose_name='Максимальное количество людей'),
        ),
        migrations.AlterField(
            model_name='dateprice',
            name='min_people',
            field=models.PositiveIntegerField(verbose_name='Минимальное количество людей'),
        ),
        migrations.AlterField(
            model_name='dateprice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='dateprice',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Начало'),
        ),
        migrations.AlterField(
            model_name='dateprice',
            name='status',
            field=models.CharField(choices=[('Sold out', 'Sold Out'), ('Completed', 'Completed'), ('Available', 'Available'), ('Guaranteed', 'Guaranteed')], default='Available', max_length=50, verbose_name='Cтатус'),
        ),
        migrations.AlterField(
            model_name='dateprice',
            name='tour',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='date_prices', to='tours.tour', verbose_name='Тур'),
        ),
        migrations.AlterField(
            model_name='program',
            name='body',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='program',
            name='day',
            field=models.PositiveIntegerField(verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='program',
            name='nutrition',
            field=models.TextField(verbose_name='Питание'),
        ),
        migrations.AlterField(
            model_name='program',
            name='placement',
            field=models.TextField(verbose_name='Размещение'),
        ),
        migrations.AlterField(
            model_name='program',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs', to='tours.tour', verbose_name='Тур'),
        ),
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='body',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='tours.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='excluded',
            field=models.TextField(blank=True, null=True, verbose_name='Не включено'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='included',
            field=models.TextField(blank=True, null=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tourphoto',
            name='image',
            field=models.ImageField(null=True, upload_to='tour_pictures/%Y/%m/%d/', verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='tourphoto',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tourphoto',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='tours.tour', verbose_name='Тур'),
        ),
    ]
