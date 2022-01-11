from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import Article, Category


# Register your models here.

@admin.action(description='انتشار مقالات انتخاب شده')
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='p')
    modeladmin.message_user(request, ngettext(
        '%d مقاله منتشر شد.',
        '%d مقاله منتشر شدند.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.action(description='پیش نویس شدن مقالات انتخاب شده')
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
        '%d مقاله پیش نویس شد.',
        '%d مقاله پیش نویس شدند.',
        updated,
    ) % updated, messages.SUCCESS)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'author', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', '-publish')
    actions = [make_published, make_draft]




@admin.action(description='نمایش دسته بندی های انتخاب شده')
def make_show(modeladmin, request, queryset):
    updated = queryset.update(status='True')
    modeladmin.message_user(request, ngettext(
        '%d دسته بندی نمایش داده شد.',
        '%d دسته بندی نمایش داده شدند.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.action(description='عدم نمایش دسته بندی های انتخاب شده')
def make_dont_show(modeladmin, request, queryset):
    updated = queryset.update(status='False')
    modeladmin.message_user(request, ngettext(
        '%d دسته بندی به حالت عدم نمایش درآمد.',
        '%d دسته بندی به حالت عدم نمایش درآمدند.',
        updated,
    ) % updated, messages.SUCCESS)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = ['status']
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_show, make_dont_show]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
