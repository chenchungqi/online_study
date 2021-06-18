from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from user.models import Profile
from django.http import JsonResponse

def lottery_view(request):
    context = {}
    return render(request, 'lotteryHTML.html', context)


def del_lottery_count(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile.lotteryCount -= 1
    profile.save()
    data = {}
    data['status'] = 'SUCCESS'
    data['last_count'] = profile.lotteryCount
    return JsonResponse(data)