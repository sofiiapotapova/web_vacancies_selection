from django.shortcuts import render, redirect
from .models import Vacancy, Competence
from .documents import VacDocument
from .getAPI import get_vac
from .useNeoApi import graph_add, get_percent
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import CompetenceForm


# Create your views here.


def index(request):
    vacancies = Vacancy.objects.all()
    competencies = Competence.objects.all()

    return render(request, 'core/index.html', {'title': 'Vacancies', 'vacancies': vacancies, 'competencies': competencies})


def users_page(request):
    """!@brief Renders user page.

    Gets the currently authenticated user to display and add his/her
    competences. Displays the form for adding a competence.

    @param form The form for adding the user's competence.
    """
    if request.method == 'POST':
        user = request.user
        form = CompetenceForm(request.POST)

        if form.is_valid():
            form.instance.person = request.user
            form.save()
            # return redirect('user-page')
            # competence = Competence.objects.create_competence(user, form.title_of_competence, form.level_of_competence)
    else:
        form = CompetenceForm()

    return render(request, 'core/user-page.html', {'form': form})


def search_results(request):
    """!@brief Render main page with search results.

    Displays the main page with search results which are the vacancy
    cards with all the required info.

    @param add_list The list which gets the vacancies from other services.
    @param competence_list The competence list
    @param percent The percent parameters which shows whether the vacancy fits you.
    @param vacs The param for Elasticsearch index creating
    @param graph_dict The dictionary for Neo4j graph creation
    """
    competencies = Competence.objects.all()
    comp_user = request.user
    comp_list_filer = []
    comp_num = 0
    for competence in competencies:
        if competence.person == comp_user:
            comp_list_filer.append(competence.title_of_competence)
            comp_num = comp_num + 1

    q = request.GET.get('q')
    add_list = get_vac(q)
    competence_list = []
    for vacancy_dict in add_list:
        if Vacancy.objects.filter(title_of_vacancy=vacancy_dict['name']):
            percent = get_percent(comp_list_filer, comp_num, vacancy_dict['name'])
            obj = Vacancy.objects.get(title_of_vacancy = vacancy_dict['name'])
            obj.percent = percent
            obj.save()
            continue
        else:
            percent = 0
            vacancy = Vacancy.objects.create_vacancy(vacancy_dict['name'], vacancy_dict['description'],
                                                     vacancy_dict['city'],
                                                     vacancy_dict['salary'], vacancy_dict['webSite'], percent)
            for i in vacancy_dict['description'].split(" "):
                competence_list.append(i)
            graph_dict = {"vac_name": vacancy_dict['name'], "com_name": competence_list}
            graph_add(graph_dict)
            percent = get_percent(comp_list_filer, comp_num, vacancy_dict['name'])
            obj = Vacancy.objects.get(title_of_vacancy = vacancy_dict['name'])
            obj.percent = percent
            obj.save()
            competence_list = []
    if q:
        vacs = VacDocument.search().query("match", title_of_vacancy=q)
    else:
        vacs = ''
    return render(request, 'core/search-results.html', {'vacs': vacs, 'competencies': competencies})


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



