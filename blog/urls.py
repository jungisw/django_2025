from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostdetailView, PostUpdateView, PostDeleteView

urlpatterns = [

    path('',PostListView.as_view(),name='post-list'),
    path('<int:pk>/',PostdetailView.as_view(),name='post-detail'),
    path('create/',PostCreateView.as_view(),name='post-create'),
    path('<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),












    path('category/<slug>/',views.category,name='category'),
    #path('', views.index, name='blog_index'),
    #path('<int:pk>/',views.detail),
    #path('create/', views.create, name='blog_create'),
    #path('<int:pk>/delete/', views.delete, name='blogdelete'),
    #path('<int:pk>/update/', views.update, name='blogupdate'),
    path('<int:pk>/createcomment/', views.createcomment, name='createcomment'),
    path('<int:pk>/updatecomment/', views.updatecomment, name='updatecomment'),
    path('<int:pk>/deletecomments/', views.deletecomment, name='deletecomment'),














path('createfake/', views.createfake, name='blog_create_fake'),
]