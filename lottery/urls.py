from django.urls import path
from . import views

urlpatterns = [
    path('lottery_view/', views.lottery_view, name='lottery_view'),
    path('del_lottery_count/', views.del_lottery_count, name='del_lottery_count'),
    path('save_lottery_prize/', views.save_lottery_prize, name='save_lottery_prize'),
]
