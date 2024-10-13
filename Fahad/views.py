from django.shortcuts import render

from django.http import HttpResponse

def first(request):
    return HttpResponse("Hello, world. You're at the first page.")