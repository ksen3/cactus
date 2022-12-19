from django import forms
from django.core.exceptions import ValidationError

from .models import Photos


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['title', 'slug', 'photo', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фото'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя автора'})
        }

    def clean_author(self):
        author = self.cleaned_data['author']
        if author == '':
            author = 'unknown_author'
        return author

# Форма не привязаная к модели
# class AddPhotoForm(forms.Form):
#     title = forms.CharField(label="Название", widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                             'placeholder': 'Название фото'}))
#
#     slug = forms.SlugField(label='URL', widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                       'placeholder': 'Ссылка'}))
#
#     photo = forms.ImageField(label='Выберите фото', widget=forms.ClearableFileInput(attrs={'class': 'form-control',
#                                                                                   'type': 'file',
#                                                                                   }))
#
#     author = forms.CharField(label='Автор', widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                       'placeholder': 'Имя автора'}))
