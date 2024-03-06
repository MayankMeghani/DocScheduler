from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
user =get_user_model
def homePage(request):
    return render(request,"home.html")