# from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# def home(request, page=1):
#     articles_list = Article.objects.published().order_by('-publish')
#     paginator = Paginator(articles_list, 6)
#     # page = request.GET.get('page')
#     articles = paginator.get_page(page)
#     context = {
#         # 'articles': Article.objects.filter(status='p').order_by('-publish'),
#         'articles': articles,
#         # 'category': Category.objects.filter(status=True)
#     }
#     return render(request, 'blog/article_list.html', context=context)

class ArticleList(ListView):
    # model = Article
    template_name = "blog/article_list.html"
    # context_object_name = "articles"
    queryset = Article.objects.published().order_by('-publish')
    paginate_by = 5


# def detail(request, slug):
#     context = {
#         # 'article': get_object_or_404(Article, slug=slug, status='p')
#         'article': get_object_or_404(Article.objects.published(), slug=slug)
#         # 'category': Category.objects.filter(status=True)
#     }
#     return render(request, 'blog/detail.html', context=context)

class ArticleDetail(DetailView):
    template_name = "blog/detail.html"

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()
#     paginator = Paginator(articles_list, 6)
#     articles = paginator.get_page(page)
#     context = {
#         'category': category,
#         'articles': articles,
#     }
#     return render(request, 'blog/category_list.html', context=context)


class CategoryList(ListView):
    # model = Article
    template_name = "blog/category_list.html"
    # context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    template_name = "blog/author_list.html"
    paginate_by = 5

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
