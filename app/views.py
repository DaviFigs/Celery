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
        email = request.POST.get('email')

        tk.send_invite.delay(name, email)
        return redirect('success')

    else:
        return redirect('forms')
