from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    return HttpResponse("<h1 style='color:red'>Welcome to the Meeting Planner!</h1>")

def bye(request):
    return HttpResponse("Googlebye! " + str(datetime.now()))

def about(request):
    return HttpResponse("<h1>Hi I'm Tom</h1><h3>I like rugby, fishing, and cooking </h3>")