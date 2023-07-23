'''
Generic Class based view implementation
'''
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"






# from django.shortcuts import render
# from django.http import HttpResponse

# '''
# back to basics
# -->page
# '''
# def homeVIew(request):
#     return HttpResponse("Hello there")
