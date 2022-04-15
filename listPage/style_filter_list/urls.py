from django.urls import path
from style_filter_list import views, ajax_

app_name = 'style_filter_list'
urlpatterns = [

    path('ajax/api/style', ajax_.call_style_api, name='api_style'),
    path('ajax/api/filter', ajax_.call_filter_api, name='api_filter'),
    path('ajax/api/studio', ajax_.call_studio_api, name='api_studio'),
    path('recipe', views.BeautyRecipeView.as_view(), name='recipe_view'),
    path('maincamera', views.MainCameraView.as_view(), name='maincamera_view'),
    path('sodabetadiscover', views.DiscoverView1.as_view(), name='sodabetadiscover_view'),
    #path('sodarealdiscover', views.DiscoverView2.as_view(), name='sodarealdiscover_view'),
    #path('tianyanbetadiscover', views.DiscoverView3.as_view(), name='tianyanbetadiscover_view'),
    #path('tianyanrealdiscover', views.DiscoverView4.as_view(), name='tianyanrealdiscover_view'),
    path('style', views.StyleView.as_view(), name='style_view'),
    path('sodabetastyle', views.View1.as_view(), name='sodabetastyle_view'),
    path('sodarealstyle', views.View2.as_view(), name='sodarealstyle_view'),
    path('tianyanbetastyle', views.View3.as_view(), name='tianyanbetastyle_view'),
    path('tianyanrealstyle', views.View4.as_view(), name='tianyanrealstyle_view'),
    path('filter', views.FilterView.as_view(), name='filter_view'),
    path('sodabetafilter', views.View5.as_view(), name='sodabetafilter_view'),
    path('sodarealfilter', views.View6.as_view(), name='sodarealfilter_view'),
    path('tianyanbetafilter', views.View7.as_view(), name='tianyanbetafilter_view'),
    path('tianyanrealfilter', views.View8.as_view(), name='tianyanrealfilter_view'),
    path('banner', views.View9.as_view(), name='banner_view'),
    path('styledb', views.View10.as_view(), name='styledb_view'),
    ]