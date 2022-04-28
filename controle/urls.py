from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:clube_id>', views.clube, name='clube'),
]
