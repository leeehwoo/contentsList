import requests
from django.http import JsonResponse


def call_style_api(request):
    response = requests.get("http://soda-api.snow.me/v1/style/overview")
#    response = requests.get("https://qa-soda-api.snow.me/v1/style/overview")
    return JsonResponse(response.json())

def call_filter_api(request):
    response = requests.get("http://soda-api.snow.me/v1/filter/overview")
    return JsonResponse(response.json())

def call_studio_api(request):
    response = requests.get("http://soda-api.snow.me/v1/template/overview")
    return JsonResponse(response.json())

