from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'email', 'grade', 'text']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Иван'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Иванов'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'email@example.com'}),
            'grade': forms.NumberInput(attrs={'class': 'form-range',
                                              'type': 'range',
                                              'min': 0,
                                              'max': 10,
                                              'step': 1}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10,
                                          'placeholder': 'Текст...'})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
