from django.urls import path
from style_filter_list import views

urlpatterns=[
    path('style/', views.style),
    path('filter/', views.filter),
]