from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from library.models import Book

def book(request):
    #DB 작업 query - select * from post
    books = Book.objects.all()
    return render(request,'library/lib.html', context={'books':books})
