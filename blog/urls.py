from django.urls import path
# from .views import home, detail, category
from .views import ArticleList, ArticleDetail, CategoryList, AuthorList

app_name = 'blog'
urlpatterns = [
    # path('', home, name='home'),
    path('', ArticleList.as_view(), name='home'),
    # path('page/<int:page>', home, name='home'),
    path('page/<int:page>', ArticleList.as_view(), name='home'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='detail'),
    # path('category/<slug:slug>', category, name='category'),
    path('category/<slug:slug>', CategoryList.as_view(), name='category'),
    # path('category/<slug:slug>/page/<int:page>', category, name='category'),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name='category'),
    path('author/<slug:username>', AuthorList.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name='author'),
]
