from django.shortcuts import render
from django.http.response import HttpResponse
from . import tasks as tk

def test(request):
    tk.test.delay()
    return HttpResponse ('Bem vindo')