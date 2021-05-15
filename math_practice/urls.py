from django.urls import path
from . import views

urlpatterns = [
    path('math_practice_main/', views.math_practice_main, name='math_practice_main'),
]
