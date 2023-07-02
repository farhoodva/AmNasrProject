# Generated by Django 4.2.2 on 2023-07-02 17:13

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsAndArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='uk,hk')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='بدنه خبر و مقاله')),
                ('short_description', models.CharField(default='توضیح کوتاه اتوماتیک', max_length=200, verbose_name='توضیح کوتاه')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='NewsAndArticles')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('active', models.BooleanField(default=True, verbose_name='فعال')),
                ('author', models.CharField(default='امیر نصرالله', max_length=200, verbose_name='نویسنده')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=150, null=True, verbose_name='اسلاگ')),
            ],
            options={
                'verbose_name': 'خبر و مقاله',
                'verbose_name_plural': 'اخبار و مقالات',
            },
        ),
    ]