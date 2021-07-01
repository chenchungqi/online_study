import datetime
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from read_statistics.utils import get_correctnum_rank,get_correctnum_rank2
from django.core.cache import cache
from user.models import Profile
from django.http import JsonResponse


# def get_group_rank():
#     group_rank = Profile.objects.filter().values('group_num').annotate(correct_num_sum=Sum('cquestion_sum')).order_by('-correct_num_sum')
#     print(group_rank)
#     return group_rank[:5]

def chengjiu_main(request):
    context = {}
    user = request.user
    already_get = user.profile.achievement_title
    print(already_get)
    if already_get.find('开端') != -1:
        print('开端')
        context['time_chengjiu1'] = 1
    else:
        context['time_chengjiu1'] = 0
    if already_get.find('渐入佳境') != -1:
        print('渐入佳境')
        context['time_chengjiu2'] = 1
    else:
        context['time_chengjiu2'] = 0
    if already_get.find('坚持的旅行者') != -1:
        print('坚持的旅行者')
        context['time_chengjiu3'] = 1
    else:
        context['time_chengjiu3'] = 0
    if already_get.find('精灵见了直呼内行') != -1:
        print('精灵见了直呼内行')
        context['time_chengjiu4'] = 1
    else:
        context['time_chengjiu4'] = 0
    if already_get.find('废寝忘食的旅行者') != -1:
        print('废寝忘食的旅行者')
        context['time_chengjiu5'] = 1
    else:
        context['time_chengjiu5'] = 0
    context['individual_rank'] = get_correctnum_rank2()
    # print(type(get_correctnum_rank()))
    get_correctnum_rank_list = list(get_correctnum_rank())
    # print(get_correctnum_rank_list[0].user)
    context['call_me_NO1'] = 0
    context['call_me_NO2'] = 0
    context['call_me_NO3'] = 0
    context['call_me_NO4'] = 0
    context['call_me_NO5'] = 0
    if get_correctnum_rank_list[0].user == user.profile.user:
        context['call_me_NO1'] = 1
    for i in range(1, 5):
        if get_correctnum_rank_list[i].user == user.profile.user:
            context['call_me_NO2'] = 1


    # if get_correctnum_rank_list[0].user == user.profile.user:
    #     context['call_me_NO3'] = 1
    # else:
    #     context['call_me_NO3'] = 0
    # if get_correctnum_rank_list[0].user == user.profile.user:
    #     context['call_me_NO4'] = 1
    # else:
    #     context['call_me_NO4'] = 0
    # if get_correctnum_rank_list[0].user == user.profile.user:
    #     context['call_me_NO5'] = 1
    # else:
    #     context['call_me_NO5'] = 0
    return render(request, 'chengjiu.html', context)


def method_main(request):
    context = {}
    #user = request.user
    # context['stay_methodPage_time'] = user.profile.stay_methodPage_time
    return render(request, 'method.html', context)


def load_staytime(request):
    user = request.user
    if not user.is_authenticated:
        return ErrorResponse(400, 'you were not login')
    total_stay_time = request.GET.get('already_stay_time')
    user.profile.stay_methodPage_time += int(total_stay_time)
    #print(user.profile.stay_methodPage_time)
    user.profile.save()

    data = {}
    data['status'] = 'SUCCESS'
    return JsonResponse(data)
