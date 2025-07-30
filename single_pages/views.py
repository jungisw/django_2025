from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,
                'single_pages/landing.html',
                  context={
                      'title': 'Landing',
                      'name': '홍길동',
                  })
