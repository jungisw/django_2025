from django.contrib import admin
from django.template.defaulttags import comment

from .models import Post, Category, Comment

# Register your models here.
#blog/admin.py
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)