from django.shortcuts import render
from django.http import HttpResponse

'''
back to basics
-->page 37
'''
def homeVIew(request):
    return HttpResponse("Hello there")
