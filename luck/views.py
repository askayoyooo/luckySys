from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.


def index(request):
	return HttpResponse('抽獎首页')


def lucky_member(request):
	return render(request, 'luck/luck.html')
