from django import forms
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
