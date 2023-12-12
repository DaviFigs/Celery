from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.main_form, name="forms"),
    path("processing/", views.processing, name="processing"),
    path('success/', views.succes, name='success')
]
