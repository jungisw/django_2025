from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect

from .froms import PostForm, CommentForm
from .models import Post, Category,Comment
from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content','category','uploaded_image','uploaded_file']


class PostdetailView(DetailView):
    model = Post




class PostListView(ListView):
    model = Post
    ordering = ['-pk']
    #template_name = 'blog/post_list.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'uploaded_image', 'uploaded_file']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreateView, self).form_valid(form)
        else:
            return redirect('/blog/')













# Create your views here.
def index(request):
    #DB 작업 query - select * from post
    posts = Post.objects.all().order_by('-pk')
    categories=Category.objects.all()
    return render(request,'blog/index.html',
                  context={'posts':posts,
                           'categories' : categories})

def category(request, slug):
    categories = Category.objects.all()
    if slug == 'no_category':
        posts = Post.objects.filter(category=None)
    else:
        category=Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)
    return render(request,'blog/index.html', context={'posts':posts, 'categories' : categories})

@login_required(login_url='/accounts/google/login/')
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    categories = Category.objects.all()
    commentform = CommentForm()
    return render(request,'blog/detail.html',context={'post':post, 'categories' : categories
                                                      ,'comments':comments, 'commentform':commentform})
@login_required(login_url='/accounts/google/login/')
def create(request):
    categories = Category.objects.all()
    if request.method=="POST":
        # 작성하다가 제출 버튼을 누른경우
        postform=PostForm(request.POST, request.FILES)

        if postform.is_valid():
            post1 = postform.save(commit=False)
            post1.author = request.user
            post1.save()
            return redirect('/blog/')
        # 정상값인 경우
    else: #get
        postform = PostForm()
    return render(request,'blog/postfrom.html',
                  context={'postform':postform, 'categories' : categories})

def createfake(request):
    post=Post()
    post.title = "새싹 용산구"
    post.content = "나진상가 3층"
    post.save()
    return redirect('/blog/')

#/blog/<int:pk>/delete
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/blog/')

def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method=="POST":
        postform=PostForm(request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('/blog/')
        else:
            return redirect('/blog/')
    else:
        postform=PostForm(instance=post)

    return render(request,template_name='blog/postupdatefrom.html', context={'postform':postform})

@login_required(login_url='/accounts/google/login/')
def createcomment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method=="POST":
        commentform=CommentForm(request.POST,request.FILES)
        if commentform.is_valid():
            comment1 = commentform.save(commit=False)
            comment1.author = request.user
            comment1.post = post
            comment1.save()
        return redirect(f'/blog/{post.pk}')

    else:
        commentform=CommentForm()
    return render(request,f'blog/commentform.html', context={'commentform':commentform})


def updatecomment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        commentform = CommentForm(request.POST, request.FILES, instance=comment)
        if commentform.is_valid():
            commentform.save()
            return redirect(f'/blog/{comment.post.pk}/')
    else:
        commentform = CommentForm(instance=comment)
    return render(request, template_name="blog/updatecommentform.html", context={'commentform': commentform})





def deletecomment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect(f'/blog/{comment.post.pk}/')