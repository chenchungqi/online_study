from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse


def lottery_view(request):
    context = {}
    return render(request, 'lotteryHTML.html', context)