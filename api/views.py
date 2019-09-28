from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
import os, random
from datetime import datetime
from django.conf import settings
from .apis import template_matching, diff_size_template_matching
import json


@csrf_exempt
def switch(request):
	# icon_name = ''
	result_dic = {}
	confidence_list = []
	# status = '0'
	# max_confidence =''
	# px = 0
	# py = 0
	if request.method == 'POST':
		if request.POST['imgType'] == '1' and 'imgType' in request.POST and 'icon_name' in request.POST:
			icon_name = request.POST['icon_name'] + '.png'
			if 'file' in request.FILES:
				data = request.FILES['file']
				img = data.read()
				now_time = datetime.now().strftime('%Y%m%d%H%M%S')
				random_str = "%06d" % random.randint(0, 999999)
				file_name = "{}.jpg".format(now_time + random_str)
				try:
					with open(os.path.join(settings.MEDIA_ROOT, 'img', file_name), 'wb') as f:
						f.write(img)
						pic_path = settings.BASE_DIR+'/media/img/' + file_name
						icon_path = settings.BASE_DIR + '/api/icons-dm/' + icon_name
						result_dic, confidence_list = template_matching(pic_path, icon_path)
				except Exception as e:
					print(e)
					print('faill to upload')
			if result_dic != {}:
				# print(type(result_dic))
				# print(result_dic)
				status = '1'
				max_confidence = confidence_list[0]
				px = result_dic[confidence_list[0]][0]
				py = result_dic[confidence_list[0]][1]
			else:
				max_confidence = 0
				status = 0
				px = None
				py = None
			return JsonResponse({"Status": str(status), "Confidence": str(max_confidence), 'Px': str(px), 'Py': str(py)})
		elif request.POST['imgType'] == '0' and 'imgType' in request.POST and 'icon_name' in request.POST:
			print('need handle binary image recognition')
			return JsonResponse({"Status": "0", "Confidence": "0", "Message": "cannot handle binary image"})
	else:
		# return HttpResponse('ok')
		return JsonResponse({"Status": "0", "Confidence": "0.9999", "Message": "Use GET method you can only get this info."})


@csrf_exempt
def find(request):
	# icon_name = ''
	result_dic = {}
	confidence_list = []
	# status = '0'
	# max_confidence =''
	# px = 0
	# py = 0
	if request.method == 'POST':
		if request.POST['imgType'] == '1' and 'imgType' in request.POST and 'icon_name' in request.POST:
			icon_name = request.POST['icon_name'] + '.png'
			if 'file' in request.FILES:
				data = request.FILES['file']
				img = data.read()
				now_time = datetime.now().strftime('%Y%m%d%H%M%S')
				random_str = "%06d" % random.randint(0, 999999)
				file_name = "{}.jpg".format(now_time + random_str)
				try:
					with open(os.path.join(settings.MEDIA_ROOT, 'img', file_name), 'wb') as f:
						f.write(img)
						pic_path = settings.BASE_DIR+'/media/img/' + file_name
						icon_path = settings.BASE_DIR + '/api/icons-dp/' + icon_name
						result_dic, confidence_list = diff_size_template_matching(pic_path, icon_path)
				except Exception as e:
					print(e)
					print('faill to upload')
			if result_dic != {}:
				# print(type(result_dic))
				# print(result_dic)
				status = '1'
				max_confidence = confidence_list[0]
				px = result_dic[confidence_list[0]][0]
				py = result_dic[confidence_list[0]][1]
			else:
				max_confidence = 0
				status = 0
				px = None
				py = None
			return JsonResponse({"Status": str(status), "Confidence": str(max_confidence), 'Px': str(px), 'Py': str(py)})
		elif request.POST['imgType'] == '0' and 'imgType' in request.POST and 'icon_name' in request.POST:
			print('need handle binary image recognition')
			return JsonResponse({"Status": "0", "Confidence": "0", "Message": "cannot handle binary image"})
	else:
		# return HttpResponse('ok')
		return JsonResponse({"Status": "0", "Confidence": "0.9999", "Message": "Use GET method you can only get this info."})