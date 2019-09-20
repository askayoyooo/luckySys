from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
import os, random
from datetime import datetime
from django.conf import settings

@csrf_exempt
def switch(request):
	if request.method == 'POST':
		if 'imgType' in request.POST:
			print(request.POST['imgType'])
		if 'binary' in request.POST:
			print(request.POST['binary'])
		# print(request.FILES['file'])
		if 'file' in request.FILES:

			data = request.FILES['file']
			print(data)
			img = data.read()
			now_time = datetime.now().strftime('%Y%m%d%H%M%S')
			random_str = "%06d" % random.randint(0, 999999)
			file_name = "{}.jpg".format(now_time + random_str)
			print(img)
			print(file_name)
			try:
				with open(os.path.join(settings.MEDIA_ROOT, 'img', file_name), 'wb') as f:
					f.write(img)

					pic_path = settings.HOST_URL + '/media/img/' + file_name
					res = {"pic_path": pic_path, "pic_name": file_name}
			except Exception as e:
				print(e)
				print('faill to upload')
				res = {}
		return JsonResponse({"Status":"0","Confidence":"0.9999"})
	else:
		# return HttpResponse('ok')
		return JsonResponse({"Status": "0", "Confidence": "0.9999"})