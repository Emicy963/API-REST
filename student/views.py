from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    return HttpResponse('<h1>Hello, Word</h1> <p>Im the API</p>')
