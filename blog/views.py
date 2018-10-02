#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.


def Test(request):
    #post = Article.objects.all()
    #return HttpResponse(post[0].content)
    #return HttpResponse('hello world!')
    return render(request, 'test.html', {'current_time': datetime.now()})

def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html',{'post_list': post_list})
    #return render(request, 'test.html')

def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})