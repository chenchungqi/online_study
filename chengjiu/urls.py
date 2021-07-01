from django.urls import path
from . import views

urlpatterns = [
    path('chengjiu_main/', views.chengjiu_main, name='chengjiu_main'),
    path('method_main/', views.method_main, name='method_main'),
    path('load_staytime/', views.load_staytime, name='load_staytime'),
]
