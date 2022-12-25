from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *
from .forms import *


class ArticlesView(ListView):
    queryset = Article.objects.filter(is_published=True)
    ordering = ['-updated_at']
    paginate_by = 10
    template_name = 'article/articles.html'


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/create.html'
    success_url = reverse_lazy('article:articles')


class ArticleDetailView(DetailView):
    queryset = Article.objects.filter(is_published=True)
    template_name = 'article/detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class ArticleUpdateView(UpdateView):
    queryset = Article.objects.filter(is_published=True)
    form_class = ArticleForm
    template_name = 'article/update.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


class ArticleDeleteView(DeleteView):
    queryset = Article.objects.filter(is_published=True)
    template_name = 'article/delete.html'
    success_url = reverse_lazy('article:articles')
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


# def articles(request):
#     object_list = Article.objects.filter(is_published=True)
#     paginator = Paginator(object_list, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'object_list': object_list,
#         'page_obj': page_obj,
#     }
#     return render(request, 'article/articles.html', context)
#
#
# def detail_view(request, post_slug):
#     post = get_object_or_404(Article.objects.filter(is_published=True), slug=post_slug)
#     context = {
#         'post': post
#     }
#     return render(request, 'article/detail.html', context)



