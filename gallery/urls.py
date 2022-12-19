from django.urls import path, include
from .views import *

urlpatterns = [
      path('', PhotosView.as_view(), name='gallery'),
      path('create/', PhotosCreateView.as_view(), name='create'),
      path('detail/<slug:photo_slug>/', PhotosDetailView.as_view(), name='detail'),
      path('update/<slug:photo_slug>/', PhotosUpdateView.as_view(), name='update'),
      path('delete/<slug:photo_slug>/', PhotosDeleteView.as_view(), name='delete'),
]