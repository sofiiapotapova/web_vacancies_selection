from django.shortcuts import render
from .models import Vacancy
from .documents import VacDocument
from .getAPI import get_vac

# Create your views here.


def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'core/index.html', {'title': 'Vacancies', 'vacancies': vacancies})


def users_page(request):
    return render(request, 'core/user-page.html')


def search_results(request):
    q = request.GET.get('q')
    # add_list = get_vac(q)
    if q:
        vacs = VacDocument.search().query("match", title_of_vacancy = q)
    else:
        vacs = ''
    return render(request, 'core/search-results.html', {'vacs': vacs})



