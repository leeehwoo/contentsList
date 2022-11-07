import datetime

from django.shortcuts import render, HttpResponse
from django.utils import timezone
# Create your views here.
from django.views.generic import TemplateView
from django.db.models import Q
from style_filter_list.models import Banner, Style


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

class DiscoverView1(TemplateView):
    template_name = 'discoverPageSodaBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)


class DiscoverView2(TemplateView):
    template_name = 'discoverPageSodareal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class DiscoverView3(TemplateView):
    template_name = 'discoverPageTianyanBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)


class DiscoverView4(TemplateView):
    template_name = 'discoverPageTianyanreal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class FeedView1(TemplateView):
    template_name = 'FeedPageFoodieBeta.html'
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

class FoodieFilterView1(TemplateView):
    template_name = 'FilterListPageFoodieBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class FoodieFilterView2(TemplateView):
    template_name = 'FilterListPageFoodieReal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)


class FoodieFilterView3(TemplateView):
    template_name = 'FilterListPageFoodieCnBeta.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)


class FoodieFilterView4(TemplateView):
    template_name = 'FilterListPageFoodieCnReal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)


class View10(TemplateView):
    template_name = 'bannerSodaBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)

class View11(TemplateView):
    template_name = 'bannerFoodieBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)


class View12(TemplateView):
    template_name = 'makeupSodaBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)












class View13(TemplateView):
    template_name = 'serverContentsList.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        b = self.get_context_data()
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        all = Banner.objects.all() #전체조회, 지금 상태에서는 쿼리문 바꾸는 경우
        a = Banner.objects.filter(end_display_date__gte=time_now, start_display_date__lte=time_now)
        b["banner_data"] = a
        # django filter
        # django jinja2 or template view
        return self.render_to_response(context=b)

class View14(TemplateView):
    template_name = 'serverContentsList.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #all = Banner.objects.all() #전체조회, 지금 상태에서는 쿼리문 바꾸는 경우
        filters = {"sound":True}
        a = Style.objects.filter(**filters).first()
        b = Style.objects.filter(smart_blur=True).first()
        print(a.sound)
        print(b.smart_blur)
        context["sound_data"] = [a]
        context["blur_data"] = [b]
        # django filter
        # django jinja2 or template view
        return self.render_to_response(context=context)

class View15(TemplateView):
    template_name = 'FeedPageFoodieBeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context=context)


