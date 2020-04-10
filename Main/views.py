from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import json, re, hashlib, random
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


def get_level_1(request):
    quests = QuestionLevel1.objects.all()
    answers = AnswerLevel1.objects.all()
    res=[]
    for i in quests:
        dic = {}
        dic['quest'] = i.text
        dic_first={}
        dic_first['text']=answers.filter(quest_id=i.id)[0].text
        dic_first['area']=answers.filter(quest_id=i.id)[0].area.id
        dic_first['check']=answers.filter(quest_id=i.id)[0].quest.id
        dic_second = {}
        dic_second['text'] = answers.filter(quest_id=i.id)[1].text
        dic_second['area'] = answers.filter(quest_id=i.id)[1].area.id
        dic_second['check'] = answers.filter(quest_id=i.id)[1].quest.id
        dic_fs={}
        dic_fs['first']=dic_first
        dic_fs['second']=dic_second
        dic['answers']=dic_fs
        res.append(dic)
    random.shuffle(res)
    return HttpResponse(json.dumps(res))


def get_level_2(request):
    answers=request.GET.get('answers')
    size=request.GET.get('gg')
    print('answers')
    print(answers)
    print(size)
    return HttpResponse(json.dumps(True))


def get_level_3(request):
    return HttpResponse(json.dumps(True))
