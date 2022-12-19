from django import forms
from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['cat', 'title', 'slug', 'photo', 'preview', 'text', 'author']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                     'type': 'file'}),
            'preview': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10,
                                          'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'cat': forms.Select(attrs={'class': 'form-control'})

        }
    # title = forms.CharField(label='Заголовок')
    # slug = forms.SlugField(label='URL')
    # photo = forms.ImageField(label='Фото')
    # preview = forms.CharField(label='Превью')
    # text = forms.TextInput()
    # author = forms.CharField(label='Автор')
    # is_published = forms.BooleanField(label="Публикация")
    # cat = forms.ModelChoiceField(queryset=Category.objects.all())
