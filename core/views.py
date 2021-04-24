from django.shortcuts import render, redirect
from .models import Vacancy
from .documents import VacDocument
from .getAPI import get_vac
from django.views.generic.edit import FormView
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.


def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'core/index.html', {'title': 'Vacancies', 'vacancies': vacancies})


def users_page(request):
    return render(request, 'core/user-page.html')


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


def sign(request):
    return render(request, 'core/sign.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are registered!')
            return redirect('login')
        else:
            messages.error(request, "Register Error")
    else:
        form = UserRegisterForm()

    return render(request, 'core/register.html', {'form': form})


def login(request):
    return render(request, 'core/login.html')


def logout(request):
    return render(request, 'core/logout.html')

# class RegisterFormView(FormView):
#     form_class = UserCreationForm
#     success_url = "/user-page/"
#
#     template_name = 'register.html'
#
#     def form_valid(self, form):
#         form.save()
#         return super(RegisterFormView, self).form_valid(form)
#
#     def form_invalid(self, form):
#         pass
#
#
# class LoginFormView(FormView):
#     pass
#
#
# class LogoutFormView(FormView):
#     pass