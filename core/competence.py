from django.http import JsonResponse
from .models import NeoCompetence
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def competenceDetails(request):
    if request.method == 'POST':
        # create competence
        json_data = json.loads(request.body)
        name = json_data['name']
        try:
            neo_competence = NeoCompetence(name = name)
            neo_competence.save()
            response = {
                'name': neo_competence.name
            }
            return JsonResponse(response)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)