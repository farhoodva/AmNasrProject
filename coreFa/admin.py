from django.contrib import admin

# Register your models here.
from coreFa.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'pic', 'created_at', 'active', 'author',]
    list_editable = ['active']


class GalleryImagesAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'image']


class PlansAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'image']


admin.site.register(NewsAndArticles, ArticleAdmin)
admin.site.register(GalleryImages, GalleryImagesAdmin)
admin.site.register(Plans, PlansAdmin)

admin.site.site_header = 'مدیریت بازار مرکزی حاتم'
admin.site.index_title = 'بازار مرکزی حاتم'
admin.site.site_title = 'بازار مرکزی حاتم'