from django.db import models
from django.urls import reverse


class Photos(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    photo = models.ImageField(upload_to='photos/gallery/%Y/%m/%d', verbose_name="Фото")
    author = models.CharField(max_length=255, blank=True, verbose_name='Автор', default='Неизвестен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(verbose_name="Публикация", default=False)

    class Meta:
        verbose_name = 'Фотокарточка'
        verbose_name_plural = 'Фотокарточки'
        ordering = ['-updated_at']

    def __str__(self):
        return f'Photo: {self.title}'

    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={'photo_slug': self.slug})
