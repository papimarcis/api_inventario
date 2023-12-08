from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return JsonResponse({'holi': 'Hola a todos'}) 