from django.shortcuts import render, redirect
from .models import Vacancy
from .documents import VacDocument
from .getAPI import get_vac
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import CompetenceForm


# Create your views here.


def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'core/index.html', {'title': 'Vacancies', 'vacancies': vacancies})


def users_page(request):
    if request.method == 'POST':
        pass
    else:
        form = CompetenceForm()

    return render(request, 'core/user-page.html', {'form': form})


def search_results(request):
    q = request.GET.get('q')
    add_list = get_vac(q)
    for vacancy_dict in add_list:
        if Vacancy.objects.filter(title_of_vacancy=vacancy_dict['name']):
            continue
        else:
            vacancy = Vacancy.objects.create_vacancy(vacancy_dict['name'], vacancy_dict['description'],
                                                 vacancy_dict['city'],
                                                 vacancy_dict['salary'], vacancy_dict['webSite'])
    if q:
        vacs = VacDocument.search().query("match", title_of_vacancy=q)
    else:
        vacs = ''
    return render(request, 'core/search-results.html', {'vacs': vacs})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You are registered!')
            return redirect('home')
        else:
            messages.error(request, "Register Error")
    else:
        form = UserRegisterForm()

    return render(request, 'core/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'core/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

