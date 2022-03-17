import datetime

from django.shortcuts import render, HttpResponse
from django.utils import timezone
# Create your views here.
from django.views.generic import TemplateView
from django.db.models import Q
from style_filter_list.models import Banner


class BeautyRecipeView(TemplateView):
    template_name = 'beautyRecipePage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)


class MainCameraView(TemplateView):
    template_name = 'mainCameraPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class DiscoverView(TemplateView):
    template_name = 'discoverPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class StyleView(TemplateView):
    template_name = 'mainStyleListPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)



class FilterView(TemplateView):
    template_name = 'mainFilterListPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View1(TemplateView):
    template_name = 'mainStyleListPageSodaBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View2(TemplateView):
    template_name = 'mainStyleListPageSodaReal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View3(TemplateView):
    template_name = 'mainStyleListPageTianyanBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View4(TemplateView):
    template_name = 'mainStyleListPageTianyanReal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)


class View5(TemplateView):
    template_name = 'mainFilterListPageSodaBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View6(TemplateView):
    template_name = 'mainFilterListPageSodaReal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View7(TemplateView):
    template_name = 'mainFilterListPageTianyanBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View7(TemplateView):
    template_name = 'mainFilterListPageTianyanReal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View8(TemplateView):
    template_name = 'mainFilterListPageTianyanBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View9(TemplateView):
    template_name = 'serverContentsList.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        b = self.get_context_data()
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #all = Banner.objects.all()
        a = Banner.objects.filter(end_display_date__gte=time_now, start_display_date__lte=time_now)
        b["banner_data"] = a
        # django filter
        # django jinja2 or template view
        return self.render_to_response(context=b)

