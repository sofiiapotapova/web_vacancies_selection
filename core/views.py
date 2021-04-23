from django.shortcuts import render
from .models import Vacancy
from .models import User
# Create your views here.


def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'core/index.html', {'title': 'Vacancies', 'vacancies': vacancies})


def users_page(request):
    return render(request, 'core/user-page.html')
