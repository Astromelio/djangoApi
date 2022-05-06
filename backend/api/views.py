from django.shortcuts import render
from django.http import JsonResponse
import model1
import json


# Create your views here.

def api_solve_list(request, *args, **kwargs):
    body = request.body
    try:
        data = json.loads(body)
    except:
        pass
    if "iteraciones" in data.keys():
        iteraciones = data["iteraciones"]
    else:
        iteraciones = 1000
    if "new_list" in data.keys():
        new_list = list(data["new_list"])
    else:
        new_list = 0


    respuesta = model1.resolver_problema(iteraciones,new_list)
    return JsonResponse({"numero": respuesta})
