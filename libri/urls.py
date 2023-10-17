from django.urls import path
from . import views

urlpatterns = [

    path('libri/', views.libri),
    path('home/', views.home),
    path('base/', views.prova),
    path('libri/acquista/', views.acquista),
    path('libri/home/', views.home),
]