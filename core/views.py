from django.shortcuts import render, redirect
from .models import Vacancy, NeoVacancy, NeoCompetence
from .documents import VacDocument
from .getAPI import get_vac
from .useNeoApi import graph_add
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import CompetenceForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


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
    competence_list = []
    for vacancy_dict in add_list:
        if Vacancy.objects.filter(title_of_vacancy=vacancy_dict['name']):
            continue
        else:
            vacancy = Vacancy.objects.create_vacancy(vacancy_dict['name'], vacancy_dict['description'],
                                                     vacancy_dict['city'],
                                                     vacancy_dict['salary'], vacancy_dict['webSite'])
            for i in vacancy_dict['description'].split(" "):
                competence_list.append(i)
            graph_dict = {"vac_name": vacancy_dict['name'], "com_name": competence_list}
            graph_add(graph_dict)
            competence_list = []
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


# @csrf_exempt
# def vacancyDetails(request):
#     if request.method == 'POST':
#         # create vacancy
#         json_data = json.loads(request.body)
#         name = json_data['name']
#         try:
#             neo_vacancy = NeoVacancy(name=name)
#             neo_vacancy.save()
#             response = {
#                 "uid": neo_vacancy.uid,
#             }
#             return JsonResponse(response)
#         except:
#             response = {"error": "Error occerred"}
#             return JsonResponse(response, safe=False)
#
#
# @csrf_exempt
# def competenceDetails(request):
#     if request.method == 'POST':
#         # create competence
#         json_data = json.loads(request.body)
#         name_competence = json_data['name']
#         try:
#             neo_competence = NeoCompetence(name_competence = name_competence)
#             neo_competence.save()
#             response = {
#                 'name': neo_competence.name
#             }
#             return JsonResponse(response)
#         except:
#             response = {"error": "Error occurred"}
#             return JsonResponse(response, safe=False)
#
#
# @csrf_exempt
# def connectVaC(request):
#     if request.method == 'PUT':
#         json_data = json.loads(request.body)
#         uid = json_data['uid']
#         name_competence = json_data['name_competence']
#         try:
#             neo_vacancy = NeoVacancy.nodes.get(uid=uid)
#             neo_competence = NeoCompetence.nodes.get(name_competence=name_competence)
#             res = neo_vacancy.neo_competence.connect(neo_competence)
#             response = {"result": res}
#             return JsonResponse(response, safe=False)
#         except:
#             response = {"error": "Error occurred"}
#             return JsonResponse(response, safe=False)