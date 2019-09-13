from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from users import models


def index(request):

	activities = models.Activity.objects.all()
	if request.method == "GET":
		print(activities)
		return render(request, 'activities/index.html',{'activities': activities})


def detail(request, activity_id):
	print(activity_id)
	return render(request,'activities/detail.html')


def detail_edit(request, activity_id):
	return render(request,'activities/detail_edit.html',{'activity_id':activity_id})


def upload_image(request,activity_id):
	if request.method =='POST':
		print(request.FILES)

	return HttpResponse('OK')
