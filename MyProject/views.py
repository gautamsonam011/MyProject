from django.shortcuts import render
from django.http import HttpResponse

def first_point(request):
    resp = HttpResponse('<h2 style = "color:green">Hey Guys! This is django Page</h2>')
    return resp