from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html', locals())


'''def homepage(request):
    posts = Post.objects.all()
    posts_lists = list()
    for counter, post in enumerate(posts):
        posts_lists.append(f'No. {counter}-{post} <br>')
        return HttpResponse(posts_lists) '''
