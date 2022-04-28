from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:clube_nome', views.clube, name='clube'),
]
