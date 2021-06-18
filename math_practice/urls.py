from django.urls import path
from . import views

urlpatterns = [
    path('math_practice_main/', views.math_practice_main, name='math_practice_main'),
    path('get_study_model/', views.get_study_model, name='get_study_model'),
    path('update_lottery_count/', views.update_lottery_count, name='update_lottery_count'),
]
