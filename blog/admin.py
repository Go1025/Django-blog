#coding=utf-8

from django.contrib import admin
from blog.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date_time')

admin.site.register(Article,ArticleAdmin)
