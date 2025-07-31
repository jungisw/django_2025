from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from library.models import Book

def index(request):
    #DB 작업 query - select * from post
    boooks = Book.objects.all()
    return render(request,'library/index.html', context={'books':books})
