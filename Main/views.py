from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# from django.core.files.storage import FileSystemStorage
import json, re, hashlib, random, timeit, datetime
from django.db.models import Q
# from django.contrib.auth import authenticate, login, logout, hashers
# from django.core.validators import validate_email
# from django.db import transaction
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from docxtpl import DocxTemplate
from django.conf import settings
# from uuslug import slugify
from django.core.files.storage import FileSystemStorage


def Main(request):
    page_name = 'Main'
    return render(request, 'Main.html', locals())


def Start_test(request):
    return render(request, 'Test.html', locals())


def get_dict(dct, quest, num):
    res = []
    for i in dct:
        if quest == i['quest_id']:
            res.append(i)
    return res[num]['area_id'], res[num]['text']


def get_level_1(request):
    quests = list(QuestionLevel1.objects.values())
    answers = list(AnswerLevel1.objects.values())
    res = []
    for i in quests:
        dic = {}
        dic['quest'] = i['text']
        l = [0, 1]
        random.shuffle(l)
        dic_first = {}
        dic_first['check'] = i['id']
        dic_first['area'], dic_first['text'] = get_dict(answers, i['id'], l[0])
        dic_second = {}
        dic_second['check'] = i['id']
        dic_second['area'], dic_second['text'] = get_dict(answers, i['id'], l[1])
        dic_fs = {}
        dic_fs['first'] = dic_first
        dic_fs['second'] = dic_second
        dic['answers'] = dic_fs
        res.append(dic)
    random.shuffle(res)
    return HttpResponse(json.dumps(res))


def get_level_2(request):
    print('level 2')
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
    if count_fail > 1:
        return HttpResponse(json.dumps(False))
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
    # print('res_quest')
    # print(res_quest)
    return HttpResponse(json.dumps(res_quest))


def get_level_3(request):
    # print('level 3')
    answers = json.loads(request.GET.get('answers'))
    # print(answers)
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
    # print('dic')
    # print(dic)

    # dic = {1: 0, 3: 10, 5: 10,6:10, 7:9}

    lst_dic = list(dic.values())
    lst_dic.sort(reverse=True)
    # print('lst_dic')
    # print(lst_dic)

    result = []
    for key, value in dic.items():
        if value == lst_dic[0]:
            result.append(key)

    if len(result) == 1:
        conclusion,conc_id,profs = get_conclusion(result[0])
        return HttpResponse(json.dumps([True, [conclusion,conc_id,profs]]))
    else:
        quests = list(QuestionLevel3.objects.filter(area_id__in=result).values('area_id', 'text'))
        list_quest_3 = []
        for i in range(len(result)):
            list_quest_3.append([])
        for i in quests:
            list_quest_3[result.index(i['area_id'])].append(i)
        min_cat = 0
        for i in list_quest_3:
            if len(i) > min_cat:
                min_cat = len(i)
        res_quest = []
        for i in range(min_cat):
            for j in list_quest_3:
                if j[i]:
                    res_quest.append(j[i])
                else:
                    continue
        # print('res_quest 3')
        # print(res_quest)
        return HttpResponse(json.dumps(res_quest))


def get_result(request):
    # print('level 3')
    answers = json.loads(request.GET.get('answers'))
    # print(answers)
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
    # print('dic')
    # print(dic)

    # dic = {1: 0, 3: 10, 5: 10,6:10, 7:9}

    lst_dic = list(dic.values())
    lst_dic.sort(reverse=True)
    # print('lst_dic')
    # print(lst_dic)

    result = []
    for key, value in dic.items():
        if value == lst_dic[0]:
            result.append(key)

    if len(result) == 1:
        conclusion, con,profs = get_conclusion(result[0])
        # return HttpResponse(json.dumps([True, conclusion]))
    else:
        conclusion, con,profs = get_conclusion(result[0], result[1])
        if len(result) > 2:
            shit = CheckTable(date=datetime.datetime.now(), count=len(result))
            shit.save()
    return HttpResponse(json.dumps([conclusion, con,profs]))


def get_conclusion(first, second=False):
    # print(first)
    # print(second)
    if second:
        # qr=Q()
        conc = Conclusions.objects.filter(Q(first_area=first) | Q(second_area=first),
                                          Q(first_area=second) | Q(second_area=second))[0]
        # print(conc)
    else:
        conc = Conclusions.objects.filter(first_area=first)[0]

    try:
        results = TestingResults.objects.get(conc_id=conc.id)
        results.count = results.count + 1
        results.save()
    except:
        res = TestingResults(conc_id=conc.id, count=1)
        res.save()
    profs=Professions.objects.filter(conclusionsprofessions__conc_id=conc.id)
    pr=[]
    for i in profs:
        p={}
        p['name']=i.name
        p['desc']=i.text
        pr.append(p)
    return conc.text, conc.id, pr


def get_file_result(request):
    try:
        name = str(request.GET.get('name'))
        surename = str(request.GET.get('surename'))
        patr = str(request.GET.get('patr'))
        test_time = str(request.GET.get('time')).split('.')
        conc = int(request.GET.get('conc'))
        if len(name) < 2 or len(surename) < 2 or len(patr) < 2 or len(test_time) != 2:
            return HttpResponse(json.dumps([False, 'Заполните поля!']))
        test_time = str(test_time[0]) + ' минут ' + str(test_time[1]) + ' секунд'
        text = Conclusions.objects.get(id=conc).text
        date = datetime.datetime.now()
        doc = DocxTemplate('Rezultat.docx')
        context = {
            'name': name,
            'surename': surename,
            'patr': patr,
            'date': date.strftime('%d.%m.%Y %H:%M:%S'),
            'test_time': test_time,
            'text': text
        }
        doc.render(context)
        filename = 'Результат_' + surename + '_' + name + '_' + date.strftime('%d%m%Y_%H%M%S_%f') + '.docx'
        path = 'media/result_files/'
        file = path + filename
        doc.save(file)
        fs = FileSystemStorage()
        rl = fs.url(file).replace('/media/media', 'media')
        link_file = 'http://' + request.get_host() + '/' + rl
        return HttpResponse(json.dumps([True, link_file]))
    except:
        return HttpResponse(json.dumps([False, 'Произошла ошибка, попробуйте позже!']))
