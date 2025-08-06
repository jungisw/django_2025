from django.urls import path
from . import views



urlpatterns = [

    path('', views.example, name='example'),
    path('helloAPI/', views.helloAPI, name='helloAPI'),
    path('postAPI/<int:pk>/', views.postAPI, name='postAPI'),
    path('blogAPI/', views.blogAPI, name='blogAPI'),
]