from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def users_page(request):
    return render(request, 'core/user-page.html')
