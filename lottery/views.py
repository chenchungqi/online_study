from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from user.models import Profile
from django.http import JsonResponse
import random


def lottery_view(request):
    context = {}
    return render(request, 'lotteryHTML.html', context)


def del_lottery_count(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile.lotteryCount -= 1

    lotteryModel_str = profile.lottery_model
    #print(lotteryModel_str)
    if lotteryModel_str == '':
        lotteryModel_str = '0,1,1,1,1,1,4,4,4,4,4,2,2,2,2,5,5,5,5,5'
        lotteryModel_list = lotteryModel_str.split(',')
        random.shuffle(lotteryModel_list)
    else:
        lotteryModel_list = lotteryModel_str.split(',')

    now_lottery = lotteryModel_list.pop()
    #print(now_lottery)
    #print(lotteryModel_list)
    str1 = ','.join(lotteryModel_list)
    profile.lottery_model = str1
    profile.save()

    data = {}
    data['status'] = 'SUCCESS'
    data['last_count'] = profile.lotteryCount
    data['now_lottery'] = now_lottery
    return JsonResponse(data)


def save_lottery_prize(request):
    awards = request.GET.get('awards')
    profile, created = Profile.objects.get_or_create(user=request.user)
    if int(awards) == 1:
        profile.diamond += 1
    elif int(awards) == 2:
        profile.diamond_pieces += 1
    else:
        data['status'] = 'ERROR'
        return JsonResponse(data)
    profile.save()
    data = {}
    data['diamondCount'] = profile.diamond
    data['diamondPiecesCount'] = profile.diamond_pieces
    data['status'] = 'SUCCESS'

    return JsonResponse(data)

