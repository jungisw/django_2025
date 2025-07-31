from django import forms
from blog.models import Post



class PostForm(forms.ModelForm):
    class Meta:    # 클래스 설명해주는 정보
        model = Post
        fields = ['title', 'content','uploaded_image', 'uploaded_file']

