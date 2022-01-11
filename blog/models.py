from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.html import format_html

from extensions.utils import jalali_converter


# my managers:
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.SET_NULL,
                               related_name="children", verbose_name="زیر دسته")
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود ؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["parent__id", "position"]

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    # estefade az methode zir baraye in ke zire har post faghat # category haee ra neshan dahad ke status=True darand.
    # def category_published(self):
    #     return self.category.filter(status=True)

    def thumbnail_tag(self):
        return format_html(f"<img width='100px' height='75px' style='border-radius:5px;' src='{self.thumbnail.url}'>")

    def category_to_str(self):
        return '، '.join([category.title for category in self.category.active()])

    category_to_str.short_description = "دسته بندی"

    objects = ArticleManager()
