from django.shortcuts import render

from blog.models import Post


# Create your views here.
def index(request):
    #DB 작업 query - select * from post
    posts = Post.objects.all()
    return render(request,'blog/index.html', context={'posts':posts})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,'blog/detail.html',context={'post':post})