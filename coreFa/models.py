from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.urls import reverse


class NewsAndArticles(models.Model):
    title = models.CharField('عنوان', max_length=200)
    body = RichTextUploadingField('بدنه خبر و مقاله', null=True, blank=True)
    short_description = models.CharField('توضیح کوتاه',
                                                 default='توضیح کوتاه اتوماتیک', max_length=200)
    pic = models.ImageField(upload_to='NewsAndArticles', null=True, blank=True)
    created_at = models.DateTimeField('تاریخ ایجاد',auto_now_add=True)
    active = models.BooleanField('فعال', default=True)
    author = models.CharField('نویسنده',max_length=200, default='امیر نصرالله')
    slug = models.SlugField('اسلاگ', max_length=150, allow_unicode=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'اخبار و مقالات'
        verbose_name = 'خبر و مقاله'

    def __str__(self):
        return self.title

    def get_article_detail_view(self):
        return reverse('coreFa:article-detail-view', kwargs={
            'pk': self.pk
        })

    # @classmethod
    # def slug_post_create(cls, sender, instance, created, *args, **kwargs):
    #     if created:
    #         instance.slug = instance.title.replace(' ', '-') \
    #                             .replace('.', '-') \
    #                             .replace('(', '-') \
    #                             .replace(')', '-') \
    #                             .replace(':', '-') \
    #                             .replace(',', '-') \
    #                             .replace('--', '-') \
    #                             .replace('"', '-') \
    #                             .replace("'", '-') \
    #                             .lower() + f'-{str(instance.id)}'
    #         instance.save()
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self.title.replace(' ', '-') \
    #                         .replace('.', '-') \
    #                         .replace('(', '-') \
    #                         .replace(')', '-') \
    #                         .replace(',', '-') \
    #                         .replace(':', '-') \
    #                         .replace('--', '-') \
    #                         .replace('"', '-') \
    #                         .replace("'", '-') \
    #                         .lower() + f'-{str(self.id)}'
    #         self.save()


# post_save.connect(NewsAndArticles.slug_post_create, sender=NewsAndArticles)


class GalleryImages(models.Model):
    title = models.CharField('عنوان', max_length=150, default='عکس گالری')
    image = models.ImageField('عکس', upload_to='gallery_images')
    description = models.CharField('توضیحات', max_length=150, default='توضیحات عکس')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(GalleryImages, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 400 or img.height > 300:
            output_size = (1920, 1080)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name_plural = 'عکس های گالری'
        verbose_name = 'عکس گالری'