import requests
from django.http import JsonResponse


def call_style_api(request):
    if request.method == "GET":
        app_type = request.GET.get("appType")
        if app_type == "soda_real":
            url = "http://soda-api.snow.me/v1/style/overview"
        elif app_type == "soda_beta":
            url = "https://qa-soda-api.snow.me/v1/style/overview"
        elif app_type == "tianyan_real":
            url = "https://api.tianyancam.com/v1/style/overview"
        elif app_type == "tianyan_beta":
            url = "http://qa-api.tianyancam.com/v1/style/overview"

        response = requests.get(url)
        return JsonResponse(response.json())

def call_filter_api(request):
    response = requests.get("http://soda-api.snow.me/v1/filter/overview")
    return JsonResponse(response.json())

def call_studio_api(request):
    response = requests.get("http://soda-api.snow.me/v1/template/overview")
    return JsonResponse(response.json())

#soda real style : http://soda-api.snow.me/v1/style/overview
#soda real filter : http://soda-api.snow.me/v1/filter/overview
#soda real studio : http://soda-api.snow.me/v1/template/overview

#soda beta style : https://qa-soda-api.snow.me/v1/style/overview
#soda beta filter : https://qa-soda-api.snow.me/v1/filter/overview
#soda beta studio : https://qa-soda-api.snow.me/v1/template/overview

#tianyan real style : https://api.tianyancam.com/v1/style/overview
#tianyan real filter :https://api.tianyancam.com/v1/filter/overview
#tianyan real studio :https://api.tianyancam.com/v1/template/overview

#tianyan beta style : http://qa-api.tianyancam.com/v1/style/overview
#tianyan beta filter : http://qa-api.tianyancam.com/v1/filter/overview
#tianyan beta studio : http://qa-api.tianyancam.com/v1/template/overview