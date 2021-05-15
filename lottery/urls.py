from django.urls import path
from . import views

urlpatterns = [
    path('lottery_view/', views.lottery_view, name='lottery_view'),
]
