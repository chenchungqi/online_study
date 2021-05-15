from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse


def math_practice_main(request):
    context = {}
    return render(request, 'math_practice_main.html', context)