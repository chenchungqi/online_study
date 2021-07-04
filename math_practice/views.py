from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.models import User
import random
from user.models import Profile
import collections as coll


def question_t1(count):
    llist = []
    for num in range(int(count)):
        while True:
            first = random.randint(1, 100)
            second = random.randint(1, 100)
            operator = random.choice('+-')
            if operator == '-':
                if first < second:
                    first, second = second, first
            r = str(first) + operator + str(second) + ' ='
            answer = eval(str(first) + operator + str(second))
            if answer <= 100:
                break
        r += str(answer)
        r += '&T1'
        llist.append(r)
    return llist


def question_t2(count):
    llist = []
    for num in range(int(count)):
        while True:
            operator = random.choice('*/')
            if operator == '*':
                first = random.randint(1, 9)
                second = random.randint(1, 9)
                r = str(first) + operator + str(second) + ' ='
                answer = eval(str(first) + operator + str(second))

            if operator == '/':
                while True:
                    first = random.randint(1, 9)
                    second = random.randint(1, 9)
                    if first < second:
                        first, second = second, first
                    r = str(first) + operator + str(second) + ' ='
                    answer = eval(str(first) + operator + str(second))
                    if eval(str(first) + '%' + str(second)) == 0:
                        break
            r += str(int(answer))
            r += '&T2'
            if 81 >= answer > 0:
                break
        llist.append(r)
    return llist

# t3 待完善
def question_t3(count):
    llist = []
    for num in range(int(count)):
        while True:
            operator1 = random.choice('+-*/')
            operator2 = random.choice('+-*/')
            if operator1 != '*' and operator1 != '/' and operator2 != '*' and operator2 != '/':
                first = random.randint(1, 100)
                second = random.randint(1, 100)
                third = random.randint(1, 100)
                if operator1 == '-':
                    if first < second:
                        first, second = second, first
                if operator2 == '-':
                    if second < third:
                        second, third = third, second
                r = str(first) + operator1 + str(second) + operator2 + str(third) + ' ='
                answer = eval(str(first) + operator1 + str(second) + operator2 + str(third))
                if 100 > answer > 0:
                    break
            if operator1 == '*' and operator2 == '*':
                first = random.randint(1, 9)
                second = random.randint(1, 9)
                third = random.randint(1, 9)
                r = str(first) + operator1 + str(second) + operator2 + str(third) + ' ='
                answer = eval(str(first) + operator1 + str(second) + operator2 + str(third))
                if answer < 81:
                    break
            if operator1 == '/' and operator2 == '*':
                first = random.randint(1, 9)
                second = random.randint(1, 9)
                third = random.randint(1, 9)
                r = str(first) + operator1 + str(second) + operator2 + str(third) + ' ='
                if eval(str(first) + '%' + str(second)) == 0:
                    answer = eval(str(first) + operator1 + str(second) + operator2 + str(third))
                    break
        r += str(int(answer))
        r += '&T3'
        llist.append(r)
    return llist


# 4,万以内加减法 此阶段和>100且<10000，差>0，积<=10000，商>=1且无余数
# 万以内加法（包含两数相加与三数相加）45+56、65+21+35
# 万以内减法985-128-231
# 万以内加减混合运算
def question_t4(count):
    llist = []
    for num in range(int(count)):
        operator1 = random.choice('+-')
        operator2 = random.choice('+-')
        if random.random() < 0.5:
            while True:
                first = random.randint(1, 10000)
                second = random.randint(1, 10000)
                if operator1 == '-':
                    if first < second:
                        first, second = second, first
                r = str(first) + operator1 + str(second) + ' ='
                answer = eval(str(first) + operator1 + str(second))
                if 10000 > answer > 0:
                    break
        else:
            while True:
                first = random.randint(1, 10000)
                second = random.randint(1, 1000)
                third = random.randint(1, 1000)
                if operator1 == '-':
                    if first < second:
                        first, second = second, first
                if operator2 == '-':
                    if second < third:
                        second, third = third, second
                r = str(first) + operator1 + str(second) + operator2 + str(third) + ' ='
                answer = eval(str(first) + operator1 + str(second) + operator2 + str(third))
                if 10000 > answer > 0:
                    break
        r += str(int(answer))
        r += '&T4'
        llist.append(r)
    return llist


#多位数乘除法（求余都为0） 此阶段和>100且<10000，差>0，积<=10000，商>=1且无余数
def question_t5(count):
    llist = []
    for num in range(int(count)):
        while True:
            operator = random.choice('*/')
            if operator == '*':
                first = random.randint(0, 999)
                second = random.randint(0, 100)
                r = str(first) + operator + str(second) + ' ='
                answer = eval(str(first) + operator + str(second))
            if operator == '/':
                while True:
                    first = random.randint(1, 100)
                    second = random.randint(1, 100)
                    if first < second:
                        first, second = second, first
                    r = str(first) + operator + str(second) + ' ='
                    answer = eval(str(first) + operator + str(second))
                    if eval(str(first) + '%' + str(second)) == 0:
                        break
            r += str(int(answer))
            r += '&T5'
            if 10000 >= answer > 1:
                break
        llist.append(r)
    return llist


# 6.小数加减法（加数<100且小数点后最多两位小数，差>0）
# 小数加法23.1+23.2
# 小数减法65.3-45.23
def question_t6(count):
    llist = []
    for num in range(int(count)):
        operator = random.choice('+-')
        while True:
            first = round(random.uniform(1, 100), 2)
            second = round(random.uniform(1, 100), 2)
            if operator == '-':
                if first < second:
                    first, second = second, first
            r = str(first) + operator + str(second) + ' ='
            answer = eval(str(first) + operator + str(second))
            if 100 > answer > 0:
                break
        r += str(round(answer, 2))
        r += '&T6'
        llist.append(r)
    return llist


# 7.小数乘除法  （涉及到小数的运算，结果都为小数点后最多保留三位小数）
# 小数乘法23.2*2、23.2*6.25*4
# 小数除法（除不尽保留两位小数）：6.25/2、54.1/2/3.4
def question_t7(count):
    llist = []
    operator1 = random.choice('*/')
    operator2 = random.choice('*/')
    for num in range(int(count)):
        if random.random() < 0.8:
            if operator1 == '*':
                first = round(random.uniform(1, 100), 2)
                second = round(random.uniform(1, 100), 1)
                r = str(first) + operator1 + str(second) + ' ='
                answer = eval(str(first) + operator1 + str(second))
            else:
                first = round(random.uniform(1, 100), 2)
                second = round(random.uniform(1, 100), 1)
                r = str(first) + operator1 + str(second) + ' ='
                answer = eval(str(first) + operator1 + str(second))
        else:
            if operator1 == '/' and operator2 == '/':
                first = round(random.uniform(50, 100), 2)
                second = round(random.uniform(1, 50), 1)
                third = round(random.uniform(1, 10), 1)
                r = str(first) + operator1 + str(second) + operator2 + str(third) + ' ='
                answer = eval(str(first) + operator1 + str(second) + operator2 + str(third))
            else:
                first = round(random.uniform(1, 100), 2)
                second = round(random.uniform(1, 100), 1)
                third = round(random.uniform(1, 100), 1)
                r = str(first) + operator1 + str(second) + operator2 + str(third) + ' ='
                answer = eval(str(first) + operator1 + str(second) + operator2 + str(third))
        r += str(round(answer, 2))
        r += '&T7'
        llist.append(r)
    return llist


# 8.分数加减法（和<100，差>0）
# 分数加法：1/2+4/5、1/2+3/8+6/5【是否需要再次分级，避免一个学生遇到无需通分，另一个学生遇到需要大量通分的题目】
# 分数减法：1/2-1/3、6/5-1/12-1/13
def question_t8(count):
    llist = []
    for num in range(int(count)):
        operator1 = random.choice('+-')
        operator2 = random.choice('+-')
        if random.random() < 0.5:
            while True:
                first_fenzi = random.randint(1, 20)
                first_fenmu = random.randint(1, 20)
                second_fenzi = random.randint(1, 20)
                second_fenmu = random.randint(1, 20)
                if operator1 == '-':
                    if (first_fenzi / first_fenmu) < (second_fenzi / second_fenmu):
                        first_fenzi, first_fenmu, second_fenzi, second_fenmu = second_fenzi, second_fenmu, first_fenzi, first_fenmu
                r = str(first_fenzi) + '/' + str(first_fenmu) + operator1 + str(second_fenzi) + '/' + str(
                    second_fenmu) + ' ='
                answer = eval(
                    str(first_fenzi) + '/' + str(first_fenmu) + operator1 + str(second_fenzi) + '/' + str(second_fenmu))
                if 100 > answer > 0:
                    break
        else:
            while True:
                first_fenzi = random.randint(1, 20)
                first_fenmu = random.randint(1, 20)
                second_fenzi = random.randint(1, 20)
                second_fenmu = random.randint(1, 20)
                third_fenzi = random.randint(1, 20)
                third_fenmu = random.randint(1, 20)
                if operator1 == '-':
                    if (first_fenzi / first_fenmu) < (second_fenzi / second_fenmu):
                        first_fenzi, first_fenmu, second_fenzi, second_fenmu = second_fenzi, second_fenmu, first_fenzi, first_fenmu
                if operator2 == '-':
                    if (second_fenzi / second_fenmu) < (third_fenzi / third_fenmu):
                        second_fenzi, second_fenmu, third_fenzi, third_fenmu = third_fenzi, third_fenmu, second_fenzi, second_fenmu
                r = str(first_fenzi) + '/' + str(first_fenmu) + operator1 + str(second_fenzi) + '/' + str(
                    second_fenmu) + operator2 + str(third_fenzi) + '/' + str(third_fenmu) + ' ='
                answer = eval(str(first_fenzi) + '/' + str(first_fenmu) + operator1 + str(second_fenzi) + '/' + str(
                    second_fenmu) + operator2 + str(third_fenzi) + '/' + str(third_fenmu))
                if 100 > answer > 0:
                    break
        r += str(round(answer, 2))
        r += '&T8'
        llist.append(r)
    return llist


def question_t9(count):
    llist = []
    operator1 = random.choice('*/')
    operator2 = random.choice('*/')
    for num in range(int(count)):
        if random.random() < 0.8:
            first_fenzi = random.randint(1, 20)
            first_fenmu = random.randint(1, 20)
            second_fenzi = random.randint(1, 20)
            second_fenmu = random.randint(1, 20)
            if operator1 == '*':
                r = str(first_fenzi) + '/' + str(first_fenmu) + operator1 + str(second_fenzi) + '/' + str(
                    second_fenmu) + ' ='
                answer = eval(
                    str(first_fenzi) + '/' + str(first_fenmu) + operator1 + str(second_fenzi) + '/' + str(second_fenmu))
            else:
                r = '(' + str(first_fenzi) + '/' + str(first_fenmu) + ')' + operator1 + '(' + str(
                    second_fenzi) + '/' + str(second_fenmu) + ')' + ' ='
                answer = eval('(' + str(first_fenzi) + '/' + str(first_fenmu) + ')' + operator1 + '(' + str(
                    second_fenzi) + '/' + str(second_fenmu) + ')')
        else:
            first_fenzi = random.randint(1, 20)
            first_fenmu = random.randint(1, 20)
            second_fenzi = random.randint(1, 20)
            second_fenmu = random.randint(1, 20)
            third_fenzi = random.randint(1, 20)
            third_fenmu = random.randint(1, 20)
            if operator1 == '/' or operator2 == '/':
                r = '(' + str(first_fenzi) + '/' + str(first_fenmu) + ')' + operator1 + '(' + str(
                    second_fenzi) + '/' + str(second_fenmu) + ')' + operator2 + '(' + str(third_fenzi) + '/' + str(
                    third_fenmu) + ')' + ' ='
                answer = eval('(' + str(first_fenzi) + '/' + str(first_fenmu) + ')' + operator1 + '(' + str(
                    second_fenzi) + '/' + str(second_fenmu) + ')' + operator2 + '(' + str(third_fenzi) + '/' + str(
                    third_fenmu) + ')')
            else:
                r = str(first_fenzi) + '/' + str(first_fenmu) + operator1 + str(second_fenzi) + '/' + str(
                    second_fenmu) + operator2 + str(third_fenzi) + '/' + str(third_fenmu) + ' ='
                answer = eval(str(first_fenzi) + '/' + str(first_fenmu) + operator1 + str(second_fenzi) + '/' + str(
                    second_fenmu) + operator2 + str(third_fenzi) + '/' + str(third_fenmu))
        r += str(round(answer, 2))
        r += '&T9'
        llist.append(r)
    return llist


def get_differentType_question(key, values):
    temp_list = []
    if key == 'T1':
        lista = question_t1(values)
        for each in lista:
            temp_list.append(each)
    if key == 'T2':
        lista = question_t2(values)
        for each in lista:
            temp_list.append(each)
    if key == 'T3':
        lista = question_t3(values)
        for each in lista:
            temp_list.append(each)
    if key == 'T4':
        lista = question_t4(values)
        for each in lista:
            temp_list.append(each)
    if key == 'T5':
        lista = question_t5(values)
        for each in lista:
            temp_list.append(each)
    if key == 'T6':
        lista = question_t6(values)
        for each in lista:
            temp_list.append(each)
    if key == 'T7':
        lista = question_t7(values)
        for each in lista:
            temp_list.append(each)
    if key == 'T8':
        lista = question_t8(values)
        for each in lista:
            temp_list.append(each)
    if key == 'T9':
        lista = question_t9(values)
        for each in lista:
            temp_list.append(each)
    return temp_list


def list_method(data):
    all_data = []
    for v, w in data.items():
        temp = []
        for i in range(w):
            temp.append(v)
        all_data.extend(temp)

    n = random.randint(0,len(all_data)-1)
    return all_data[n]


def get_question_method(study_model, question_counts, question_difficulty):
    question_list = []
    wrong_questions = study_model.split(',')
    #print(question_difficulty)
    #print(study_model)
    study_model_matrix = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1],
    ]
    for i in range(0, 9):
        if wrong_questions[i] != '0':
            study_model_matrix[int(question_difficulty)][i] += int(wrong_questions[i])
    ready_matrix = study_model_matrix[int(question_difficulty)]
    list1 = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9']
    data = dict(zip(list1, ready_matrix))

    dict_num = coll.defaultdict(int)
    for i in range(int(question_counts)):
        dict_num[eval("list_method(data)")] += 1

    for key, values in dict_num.items():
        #print(key, values)
        if values != 0:
            listb = get_differentType_question(key, values)
            for each in listb:
                question_list.append(each)
    random.shuffle(question_list)
    #print(question_list)
    return question_list


def SuccessResponse(study_model):
    data = {}
    data['status'] = 'SUCCESS'
    data['study_model'] = study_model
    return JsonResponse(data)


def ErrorResponse(code, message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] = message
    return JsonResponse(data)


def math_practice_main(request):
    context = {}
    if request.method == 'POST':
        # 获取数据
        input_answer = request.POST.get('input_answer', '')
        correct_answer = request.POST.get('correct_answer', '')
        question_mark = request.POST.get('question_mark', '')
        tempData = request.POST.get('tempData', '')
        user = request.user
        if user.is_staff:
            context['staff'] = 'True'
        #print('input_answer='+input_answer,'correct_answer='+correct_answer,'tempData_list='+tempData,'question_mark='+question_mark)
        if type(input_answer) == str:
            input_answer = eval(input_answer)
        if type(correct_answer) == str:
            correct_answer = eval(correct_answer)
        if round(input_answer, 2) == round(correct_answer, 2):
            context['status'] = 'RIGHT'
            user.profile.cquestion_sum += 1
            user.profile.save()
        else:
            context['status'] = 'ERROR'
            context['rightAnswer'] = correct_answer
            user.profile.wquestion_sum += 1
            user.profile.save()

            # 根据错误数据修改模型 相应错误类型权重+1
            sode = user.profile.user_study_mode
            # print(sode)
            al = sode.split(',')
            al = [int(x) for x in al]
            al[int(question_mark[1:]) - 1] += 1
            str1 = ','.join(str(i) for i in al)
            user.profile.user_study_mode = str1
            # print(str1)
            user.profile.save()

        context['tempData_list'] = tempData
        user.profile.question_num += 1
        user.profile.save()
        return JsonResponse(context)
    else:
        context['user_mode'] = '2222'  # 暂无意义
    return render(request, 'math_practice_main.html', context)

# 生成的题目类型模型
def get_study_model(request):
    user = request.user
    if not user.is_authenticated:
        return ErrorResponse(400, 'you were not login')
    study_model = user.profile.user_study_mode  #0,0,0,0,0,0,0,0,0
    # if user.profile.grade_class == '一年级':
    #     question_difficulty = 0
    # elif user.profile.grade_class == '二年级':
    #     question_difficulty = 1
    # elif user.profile.grade_class == '三年级':
    #     question_difficulty = 3
    # elif user.profile.grade_class == '四年级':
    #     question_difficulty = 5
    # elif user.profile.grade_class == '五年级':
    #     question_difficulty = 7
    # else:
    question_difficulty = user.profile.question_difficulty # 默认为0

    question_counts = request.GET.get('question_counts')

    data = {}
    data['status'] = 'SUCCESS'
    # 生成n个题目存入list
    data['question_list'] = get_question_method(study_model, question_counts, question_difficulty)

    # 将对应的错误类型模型置空
    user = request.user
    user.profile.user_study_mode = '0,0,0,0,0,0,0,0,0'
    user.profile.save()
    return JsonResponse(data)


def update_lottery_count(request):
    correct_rates = request.GET.get('correct_rates')
    learning_time = request.GET.get('total_learning_time')
    user = request.user
    questionDifficulty = user.profile.question_difficulty
    # print(questionDifficulty)
    # print(type(questionDifficulty))
    # print(learning_time)
    # print(type(learning_time))
    questionDifficulty_Alist = [200000, 200000, 200000, 320000, 400000, 440000, 640000, 720000, 800000]
    questionDifficulty_Clist = [400000, 400000, 400000, 500000, 600000, 640000, 920000, 1040000, 1140000]
    addCount = 0
    if int(correct_rates) == 100:
        addCount += 2
        score = '评分为:S'
        # 升级
        if questionDifficulty < 8:
            if questionDifficulty > 5:
                addCount += 3
            elif questionDifficulty > 2:
                addCount += 2
            else:
                addCount += 1
            user.profile.question_difficulty += 1
            user.profile.save()
    elif int(correct_rates) >= 90:
        addCount += 1
        score = '评分为:A'
        # 升级
        if questionDifficulty < 8 and int(learning_time) < questionDifficulty_Alist[questionDifficulty]:
            #print('评分为:A,并且答题速度快，升级')
            if questionDifficulty > 5:
                addCount += 3
            elif questionDifficulty > 2:
                addCount += 2
            else:
                addCount += 1
            user.profile.question_difficulty += 1
            user.profile.save()
    elif int(correct_rates) >= 60:
        score = '评分为:B'
    else:
        if int(correct_rates) < 60:
            if questionDifficulty > 0 and int(learning_time) > questionDifficulty_Clist[questionDifficulty]:
                #print('评分为:C,并且答题速度慢，降级')
                user.profile.question_difficulty -= 1
                user.profile.save()
        score = '评分为:C'
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile.lotteryCount += addCount
    profile.group_question_sum += 1
    profile.total_time += int(learning_time)
    # print(profile.total_time)
    # print(user.is_staff)
    tips = ''
    if user.is_staff:
        chengjiu = profile.achievement_title
        totalTime = profile.total_time
        if int(totalTime) >= 3600000:
            if chengjiu.find('废寝忘食的旅行者') == -1:
                profile.achievement_title += ',废寝忘食的旅行者'
                profile.lotteryCount += 1
                tips = '废寝忘食的旅行者'
        elif int(totalTime) >= 2400000:
            if chengjiu.find('精灵见了直呼内行') == -1:
                profile.achievement_title += ',精灵见了直呼内行'
                profile.lotteryCount += 1
                tips = '精灵见了直呼内行'
        elif int(totalTime) >= 1800000:
            if chengjiu.find('坚持的旅行者') == -1:
                profile.achievement_title += ',坚持的旅行者'
                profile.lotteryCount += 1
                tips = '坚持的旅行者'
        elif int(totalTime) >= 1200000:
            if chengjiu.find('渐入佳境') == -1:
                profile.achievement_title += ',渐入佳境'
                profile.lotteryCount += 1
                tips = '渐入佳境'
        elif int(totalTime) >= 600000:
            if chengjiu.find('开端') == -1:
                profile.achievement_title += '开端'
                profile.lotteryCount += 1
                tips = '开端'
        else:
            pass
        # print(profile.achievement_title)
    profile.save()
    data = {}
    data['status'] = 'SUCCESS'
    data['grades'] = score
    data['tips'] = tips
    return JsonResponse(data)
