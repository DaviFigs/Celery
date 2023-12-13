from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from . import tasks as tk

def main_form(request):
    tk.test.delay()
    return render(request, 'forms.html')

def succes(request):
    return render(request, 'success.html')

def processing(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')

        #first we have to configure the image before we send email task
        



        return redirect('success')

    else:
        return redirect('forms')
