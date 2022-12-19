from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('read/<slug:post_slug>/', ArticleDetailView.as_view(), name='detail'),
    path('update/<slug:post_slug>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<slug:post_slug>/', ArticleDeleteView.as_view(), name='delete'),
]
