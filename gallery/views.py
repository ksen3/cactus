from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Photos
from .forms import *


class PhotosView(ListView):
    # model = Photos
    paginate_by = 15
    queryset = Photos.objects.filter(is_published=True)
    ordering = ['-updated_at']
    template_name = 'gallery/gallery.html'


class PhotosCreateView(CreateView):
    form_class = AddPhotoForm
    template_name = 'gallery/create.html'
    success_url = reverse_lazy('gallery:gallery')


class PhotosDetailView(DetailView):
    queryset = Photos.objects.filter(is_published=True)
    template_name = 'gallery/detail.html'
    slug_url_kwarg = 'photo_slug'
    context_object_name = 'photo_item'


class PhotosUpdateView(UpdateView):
    model = Photos
    form_class = AddPhotoForm
    template_name = 'gallery/update.html'
    slug_url_kwarg = 'photo_slug'
    success_url = reverse_lazy('gallery:gallery')
    context_object_name = 'photo_item'


class PhotosDeleteView(DeleteView):
    model = Photos
    template_name = 'gallery/delete.html'
    context_object_name = 'photo_item'
    slug_url_kwarg = 'photo_slug'
    success_url = reverse_lazy('gallery:gallery')


# def galleryDetail(request, photo_slug):
#     photo_item = get_object_or_404(Photos, slug=photo_slug)
#     return render(request, 'gallery/detail.html', {'photo_item': photo_item})
#
#
# def photosCreate(request):
#     if request.method == 'POST':
#         form = AddPhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 # Photos.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('gallery')
#             except:
#                 form.add_error(None, 'Ошибка добавления. Проверьте правильность заполнения формы.')
#     else:
#         form = AddPhotoForm()
#
#     return render(request, 'gallery/create.html', {'form': form})





