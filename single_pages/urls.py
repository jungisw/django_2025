#from sesac_django_project.urls import urlpatterns

from django.urls import path
from.import views
urlpatterns=[
    path('',views.landing,name='landing'),
    path('aboutme/',views.aboutme,name='about'),


]