from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import json, re, hashlib, random, timeit
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, hashers
from django.core.validators import validate_email
from django.db import transaction
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.conf import settings


def Main(request):
    return render(request, 'Main.html', locals())


def Start_test(request):
    return render(request, 'Test.html', locals())


def select_bd(request):
    quests = QuestionLevel1.objects.all()
    answers = AnswerLevel1.objects.all()
    return True


def get_level_1(request):
    # print(timeit.timeit(stmt='quests = QuestionLevel1.objects.all()',setup='from .models import QuestionLevel1',number=1))
    quests = QuestionLevel1.objects.select_related()
    answers = AnswerLevel1.objects.select_related()
    # print(str(quests.query))

    # answers = AnswerLevel1.objects.all()
    # print(timeit.timeit(stmt="""
    res = []
    for i in quests:
        dic = {}
        dic['quest'] = i.text
        l = [0, 1]
        random.shuffle(l)
        dic_first = {}
        dic_first['text'] = answers.filter(quest_id=i.id)[l[0]].text
        dic_first['area'] = answers.filter(quest_id=i.id)[l[0]].area.id
        dic_first['check'] = answers.filter(quest_id=i.id)[l[0]].quest.id
        dic_second = {}
        dic_second['text'] = answers.filter(quest_id=i.id)[l[1]].text
        dic_second['area'] = answers.filter(quest_id=i.id)[l[1]].area.id
        dic_second['check'] = answers.filter(quest_id=i.id)[l[1]].quest.id
        dic_fs = {}
        dic_fs['first'] = dic_first
        dic_fs['second'] = dic_second
        dic['answers'] = dic_fs
        res.append(dic)
    random.shuffle(res)
    # """,number=1))
    return HttpResponse(json.dumps(res))


def get_level_2(request):
    answers = json.loads(request.GET.get('answers'))

    dic = {}
    for i in answers:
        quest = i[0]
        answer = i[1]
        dic[quest] = answer

    print(sorted(dic.items()))
    check_quests = CheckQuestion.objects.all()
    count_fail = 0
    for i in check_quests:
        if dic[i.first_quest.id] != dic[i.second_quest.id]:
            print('fail #' + str(count_fail + 1))
            count_fail += 1
    # if count_fail > 1:
    #     return HttpResponse(json.dumps(False))
    del dic[31]
    del dic[32]
    del dic[33]
    dic_val = list(dic.values())
    dic_cats = {}
    for i in range(6):
        dic_cats[i + 1] = dic_val.count(i + 1)
    val_sorted = list(dic_cats.values())
    val_sorted.sort(reverse=True)
    dic_sorted = {}
    for i in val_sorted:
        dic_sorted[i] = val_sorted.count(i)
    lst_sorted = list(dic_sorted.keys())
    res_max = []
    res_max.append(lst_sorted[0])
    if dic_sorted[lst_sorted[0]] < 2:
        res_max.append(lst_sorted[1])
    result = []
    for key, value in dic_cats.items():
        for j in res_max:
            if value == j:
                result.append(key)
    cats = list(QuestionLevel2.objects.filter(area_id__in=result).values('area_id', 'text'))
    list_quest_2 = []
    for i in range(len(result)):
        list_quest_2.append([])
    for i in cats:
        list_quest_2[result.index(i['area_id'])].append(i)
    min_cat = 0
    for i in list_quest_2:
        if len(i) > min_cat:
            min_cat = len(i)
    res_quest = []
    for i in range(min_cat):
        for j in list_quest_2:
            if j[i]:
                res_quest.append(j[i])
            else:
                continue

    # for i in res_quest:
    #     print(i)
    # print(len(res_quest))
    # qst=
    # qst_arr=qst.split('#')
    # cat_id=6
    # print(qst_arr)
    # for i in qst_arr:
    #     qs=QuestionLevel2(text=i,area_id=cat_id)
    #     # qs.save()
    #     print(qs)
    return HttpResponse(json.dumps(res_quest))


def get_level_3(request):
    answers = json.loads(request.GET.get('answers'))
    print(answers)
    dic = {}
    for i in answers:
        if i[1] == 0:
            answer = False
        else:
            answer = True
        quest = i[0]
        if dic.get(quest):
            if answer:
                dic[quest] += 1
        else:
            if answer:
                dic[quest] = 1
            else:
                dic[quest] = 0
    print(dic)

    # dic = {1: 0, 3: 10, 5: 10,6:10, 7:9}

    lst_dic = list(dic.values())
    lst_dic.sort(reverse=True)
    print('lst_dic')
    print(lst_dic)

    result=[]
    for key, value in dic.items():
        if value == lst_dic[0]:
            result.append(key)

    if lst_dic.count(lst_dic[0])>1:
        conclusion = get_conclusion(result[0], result[1])
        if len(result) > 2:
            print('gg diplom ne top')
        print(conclusion)
    else:
        conclusion = get_conclusion(result[0])
        print(conclusion)
    print(result)

    # qst='Я решительный.#Я легко поддерживаю разговор на любую тему.#Я ответственный человек.#В будущем я хотел бы иметь много связей.'
    # qst_arr=qst.split('#')
    # cat_id=6
    # print(qst_arr)
    # for i in qst_arr:
    #     qs=QuestionLevel3(text=i,area_id=cat_id)
    #     # qs.save()
    #     print(qs)
    return HttpResponse(json.dumps(True))

def get_conclusion(first,second=False):
    if second:
        # qr=Q()
        conc=Conclusions.objects.filter(Q(first_area=first)|Q(second_area=first),Q(first_area=second)|Q(second_area=second))[0].text
        # print(conc)
    else:
        conc=Conclusions.objects.filter(first_area=first)[0].text
    return conc