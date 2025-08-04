from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug>/',views.category,name='category'),
    path('', views.index, name='blog_index'),
    path('<int:pk>/',views.detail),
    path('create/', views.create, name='blog_create'),
    path('createfake/', views.createfake, name='blog_create_fake'),
    path('<int:pk>/delete/', views.delete, name='blogdelete'),
    path('<int:pk>/update/', views.update, name='blogupdate'),
    path('<int:pk>/createcomment/', views.createcomment, name='createcomment'),
    path('<int:pk>/updatecomment/', views.updatecomment, name='updatecomment'),
    path('<int:pk>/deletecomments/', views.deletecomment, name='deletecomment'),

]