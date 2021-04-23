from django.shortcuts import render
from .models import Vacancy
from .documents import VacDocument
from django.views.generic import ListView
from .models import User
# Create your views here.


def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'core/index.html', {'title': 'Vacancies', 'vacancies': vacancies})


def users_page(request):
    return render(request, 'core/user-page.html')


def search_results(request):
    q = request.GET.get('q')
    if q:
        vacs = VacDocument.search().query("match", title_of_vacancy = q)
    else:
        vacs = ''
    return render(request, 'core/search-results.html', {'vacs': vacs})


# class SearchResultsView(ListView):
#     model = Vacancy
#     template_name = 'search-results.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Vacancy.objects.filter(title_of_vacancy__icontains=query)
#         return object_list
