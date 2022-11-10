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
        elif app_type == "makeup_beta":
            url = "https://qa-content-soda-api.snow.me/v1/sticker/asset/categories?assetType=MAKEUP&position=EDIT&withAllAssets=true&dl=S"
        elif app_type == "banner_beta":
            url = "http://adg-beta.kajicam.com/adminapi/plan/list?pageNum=1&pageSize=10&gender=&userId=&level=&startDate=&endDate=&appId=soda&status=2"

        response = requests.get(url)
        return JsonResponse(response.json())

def call_filter_api(request):
    if request.method == "GET":
        app_type = request.GET.get("appType")
        if app_type == "soda_real":
            url = "http://soda-api.snow.me/v1/filter/overview"
        elif app_type == "soda_beta":
            url = "https://qa-soda-api.snow.me/v1/filter/overview"
        elif app_type == "tianyan_real":
            url = "https://api.tianyancam.com/v1/filter/overview"
        elif app_type == "tianyan_beta":
            url = "http://qa-api.tianyancam.com/v1/filter/overview"

        elif app_type == "foodie_real":
            url = "https://content-foodie-api.snow.me/v1/sticker/asset/categories?assetType=LUT_FILTER&withAllAssets=true&dl=S"
        elif app_type == "foodie_beta":
            url = "http://qa-content-foodie-api.snow.me/v1/sticker/asset/categories?assetType=LUT_FILTER&withAllAssets=true&dl=S"
        elif app_type == "foodiecn_real":
            url = "https://content-foodiecn-api.b612kaji.com/v1/sticker/asset/categories?assetType=LUT_FILTER&withAllAssets=true&dl=S"
        elif app_type == "foodiecn_beta":
            url = "http://qa-content-foodiecn-api.b612kaji.com/v1/sticker/asset/categories?assetType=LUT_FILTER&withAllAssets=true&dl=S"

        response = requests.get(url)
        return JsonResponse(response.json())

def call_studio_api(request):
    if request.method == "GET":
        app_type = request.GET.get("appType")
        if app_type == "soda_real":
            url = "http://soda-api.snow.me/v1/template/overview"
        elif app_type == "soda_beta":
            url = "https://qa-soda-api.snow.me/v1/template/overview"
        elif app_type == "tianyan_real":
            url = "https://api.tianyancam.com/v1/template/overview"
        elif app_type == "tianyan_beta":
            url = "http://qa-api.tianyancam.com/v1/template/overview"

        elif app_type == "foodie_real":
            url = "http://foodie-api.snow.me/v1/template/overview"
        elif app_type == "foodie_beta":
            url = "https://api-beta-foodie.snow.me/foodie/api/category/list?os=a&appVersion=4.4.1"
        elif app_type == "foodiecn_real":
            url = "http://foodie-api.snow.me/v1/template/overview"
        elif app_type == "foodiecn_beta":
            url = "http://qa-soda-api.snow.me/v1/template/overview"

        response = requests.get(url)
        return JsonResponse(response.json())




