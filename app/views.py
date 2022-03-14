from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello  {nome} de {idade} anos </h1>')