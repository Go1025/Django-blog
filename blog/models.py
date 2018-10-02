#coding=utf-8
from django.db import models
#from ueditor import controller
from tinymce.models import HTMLField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50) #题目
    category = models.CharField(max_length=50, blank=True) #博客标签
    date_time = models.DateTimeField(auto_now_add=True) #博客日期
    content = HTMLField()

def __str__(self):
    return self.title

class Meta:
    ordering = ['-date_time']