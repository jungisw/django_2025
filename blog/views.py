from django.shortcuts import render, redirect

from .froms import PostForm
from .models import Post


# Create your views here.
def index(request):
    #DB 작업 query - select * from post
    posts = Post.objects.all().order_by('-pk')
    return render(request,'blog/index.html', context={'posts':posts})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,'blog/detail.html',context={'post':post})

def create(request):
    if request.method=="POST":
        # 작성하다가 제출 버튼을 누른경우
        postform=PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post1 = postform.save(commit=False)
            post1.title = post1.title + "홍길동 만세"
            post1.save()
            return redirect('/blog/')
        # 정상값인 경우
    else: #get
        postform = PostForm()
    return render(request,'blog/postfrom.html',
                  context={'postform':postform})

def createfake(request):
    post=Post()
    post.title = "새싹 용산구"
    post.content = "나진상가 3층"
    post.save()
    return redirect('/blog/')