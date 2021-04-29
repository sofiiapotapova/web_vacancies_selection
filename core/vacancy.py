from django.http import JsonResponse
from .models import NeoVacancy
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def vacancyDetails(request):
    if request.method == 'POST':
        # create vacancy
        json_data = json.loads(request.body)
        name = json_data['name']
        try:
            neo_vacancy = NeoVacancy(name=name)
            neo_vacancy.save()
            response = {
                "uid": neo_vacancy.uid,
            }
            return JsonResponse(response)
        except:
            response = {"error": "Error occerred"}
            return JsonResponse(response, safe=False)
