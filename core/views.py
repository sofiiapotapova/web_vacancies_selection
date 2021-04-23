from django.shortcuts import render
from .models import Vacancy
# Create your views here.


def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'core/index.html', {'title': 'Main page of site', 'vacancies': vacancies})


def users_page(request):
    return render(request, 'core/user-page.html')
