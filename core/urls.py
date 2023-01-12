from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insert, name='insert'),
    path('display', views.display, name='display'),
    path('registrationform', views.registration, name='registration')
]