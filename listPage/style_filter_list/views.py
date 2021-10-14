from django.shortcuts import render, HttpResponse

# Create your views here.

def style(request):
    return render(request, 'style_filter_list/styleList.html')

def filter(request):
    return render(request, 'style_filter_list/filterList.html')