from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import TemplateView


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