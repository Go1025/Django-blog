#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^test/', views.Test, name='test'),
    url(r'post/(?P<id>\d+)/$',views.Detail,name='detail'),
]