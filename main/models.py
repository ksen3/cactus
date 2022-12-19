from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
from django.db import models
from django.urls import reverse


class MainContent(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    photo = models.ImageField(upload_to='photos/main/%Y/%m/%d', verbose_name='Фото')
    text = models.CharField(max_length=255, verbose_name='Текст')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=False, verbose_name='Публикация')

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
        ordering = ['updated_at']

    def __str__(self):
        return self.title

class Review(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=40, help_text="Введите ваше имя")
    last_name = models.CharField(verbose_name="Фамилия", max_length=40, help_text="Введите вашу фамилию")
    birth = models.DateField(verbose_name="Дата рождения", help_text="Введите дату рождения", blank=True)
    username = models.CharField(verbose_name="Ник", max_length=40, help_text="Введите ваш никнейм", blank=True)
    email = models.EmailField(verbose_name="E-mail", validators=[EmailValidator(message='Введите правильный адрес')])
    text = models.TextField(verbose_name="Текст обращения", blank=True)
    grade = models.PositiveSmallIntegerField(default=5,
                                             validators=[
                                                 MaxValueValidator(10),
                                                 MinValueValidator(1),
                                             ],
                                            help_text="Оценка от 0 до 10",
                                            verbose_name="Оценка")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)


    def __str__(self):
        return f'Отзыв №{self.pk}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
