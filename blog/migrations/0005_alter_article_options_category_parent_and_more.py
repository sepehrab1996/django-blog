# Generated by Django 4.0 on 2021-12-30 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish'], 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.category', verbose_name='زیر دسته'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]
