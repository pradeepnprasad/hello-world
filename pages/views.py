from django.shortcuts import render
from django.http import HttpResponse

'''home page view'''
def homePageView(request):
    return HttpResponse("Welcome to django!")
# Create your views here.
