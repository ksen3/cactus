from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    # path('gallery/', gallery, name='gallery'),
    path('contacts/', contacts, name='contacts'),
]
