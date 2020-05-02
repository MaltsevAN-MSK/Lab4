from .models import Article
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django import template

# Create your views here.

#def home(request):
#    return render (request, 'templates/index.html')
def archive(request):
    return render(request, 'templates/archive.html', {"posts":Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
