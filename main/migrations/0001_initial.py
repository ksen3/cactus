# Generated by Django 4.1.4 on 2022-12-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('photo', models.ImageField(upload_to='photos/main/%Y/%m/%d', verbose_name='Фото')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
                'ordering': ['updated_at'],
            },
        ),
    ]
