from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('<int:clube_id>', views.clube, name='clube'),
=======
>>>>>>> 0c47fd46b6934b46aaaf3291c5edf8dde05cb55c
]
