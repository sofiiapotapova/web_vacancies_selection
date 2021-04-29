from django.http import JsonResponse
from .models import NeoCompetence, NeoVacancy
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def connectVaC(request):
    pass