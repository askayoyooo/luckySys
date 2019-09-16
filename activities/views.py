from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from users import models
import os, random
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse


def index(request):

	activities = models.Activity.objects.all()
	if request.method == "GET":
		print(activities)
		return render(request, 'activities/index.html',{'activities': activities})


def detail(request, activity_id):
	activity = get_object_or_404(models.Activity, pk=activity_id )
	print(activity_id)
	return render(request,'activities/detail.html', {'activity':activity})


def detail_edit(request, activity_id):
	activity = get_object_or_404(models.Activity, pk=activity_id)
	if request.method =='POST':
		content = request.POST['content']
		name = request.POST['title']
		activity.content=content
		activity.name = name
		activity.save()
	else:
		content = activity.content
	return render(request,'activities/detail_edit.html',{'activity_id':activity_id, 'content':content, 'activity':activity})


def upload_image(request):
	if request.method =='POST':
		print(request.FILES)
		print(request.FILES['file'])
		data = request.FILES['file']
		img = data.read()
		now_time = datetime.now().strftime('%Y%m%d%H%M%S')
		random_str = "%06d" % random.randint(0,999999)
		file_name = "{}.png".format(now_time+random_str)
		print(img)
		print(file_name)
		try:
			with open(os.path.join(settings.MEDIA_ROOT,'img',file_name),'wb') as f:
				f.write(img)

				pic_path = settings.HOST_URL+'/media/img/'+file_name
				res ={"pic_path": pic_path, "pic_name":file_name}
		except Exception as e:
			print(e)
			print('faill to upload')
			res = {}

		return JsonResponse(res)
