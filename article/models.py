from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/article/%Y/%m/%d', blank=True, verbose_name='Фото')
    preview = models.CharField(max_length=255, blank=True, verbose_name='Превью')
    text = models.TextField(verbose_name='Текст')
    author = models.CharField(max_length=255, blank=True, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(verbose_name="Публикация", default=False)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    
    class Meta:
        verbose_name='Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-updated_at']

    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'post_slug': self.slug})


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name='Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name