from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:    # 클래스 설명해주는 정보
        model = Post
        fields = ['title', 'author', 'content', 'category', 'uploaded_image', 'uploaded_file']




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','content']


