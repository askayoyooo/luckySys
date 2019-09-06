from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from users import models


def index(request):

	activities = models.Activity.objects.all()
	if request.method == "GET":

		return render(request, 'activities/index.html',{'activities': activities})