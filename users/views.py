from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile, Site
from django.contrib import auth
from .forms import RegistrationForm, LoginForm, ProfileForm, PwdChangeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.


def index(request):
	return HttpResponse('用戶首页')


@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/accounts/login/")


@login_required
def pwd_change(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	user_logined = request.user
	if user != user_logined:
		return HttpResponse('You have no permission on this page')

	if request.method == "POST":
		form = PwdChangeForm(request.POST)

		if form.is_valid():

			password = form.cleaned_data['old_password']
			username = user.username

			user = auth.authenticate(username=username, password=password)

			if user is not None and user.is_active:
				new_password = form.cleaned_data['password2']
				user.set_password(new_password)
				user.save()
				return HttpResponseRedirect("/accounts/login/")

			else:
				return render(request, 'users/pwd_change.html', {'form': form, 'user': user, 'message': 'Old password is wrong. Try again'})
	else:
		form = PwdChangeForm()

	return render(request, 'users/pwd_change.html', {'form': form, 'user': user})



# @login_required
# def profile_update(request, user_id):
# 	user = get_object_or_404(User, pk=user_id)
# 	user_profile = get_object_or_404(UserProfile, user=user)
# 	user_logined = request.user
# 	if user != user_logined:
# 		return HttpResponse('You have no permission on this page')
# 	if request.method == "POST":
# 		form = ProfileForm(request.POST, request.FILES)
# 		print("post is on")
#
# 		if form.is_valid():
# 			user.first_name = form.cleaned_data['first_name']
# 			# user.last_name = form.cleaned_data['last_name']
# 			user.save()
#
# 			user_profile.short_number = form.cleaned_data['short_number']
# 			user_profile.phone_number = form.cleaned_data['phone_number']
# 			user_profile.avatar = form.cleaned_data['avatar']
# 			user_profile.site = Site.objects.get(id=form.cleaned_data['site_id'])
# 			user_profile.save()
#
# 			return HttpResponseRedirect(reverse('users:profile', kwargs={'user_id': user.id}))
# 	else:
# 		default_data = {'first_name': user.first_name, 'last_name': user.last_name,'short_number': user_profile.short_number, 'phone_number': user_profile.phone_number, }
# 		form = ProfileForm(default_data)
#
# 	return render(request, 'users/profile_update.html', {'form': form, 'user': user})


@login_required
def profile(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	user_profile = get_object_or_404(UserProfile, user=user)
	user_logined = request.user
	if user != user_logined:
		return HttpResponse('You have no permission on this page')
	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			user.first_name = form.cleaned_data['first_name']
			# user.last_name = form.cleaned_data['last_name']
			user.save()

			user_profile.short_number = form.cleaned_data['short_number']
			user_profile.phone_number = form.cleaned_data['phone_number']
			user_profile.experience = form.cleaned_data['experience']
			user_profile.job = form.cleaned_data['job']
			user_profile.skill = form.cleaned_data['skill']
			user_profile.education = form.cleaned_data['education']
			if form.cleaned_data['avatar'] is not None:
				user_profile.avatar = form.cleaned_data['avatar']
			else:
				print("User dose not upload avatar")
			user_profile.site = Site.objects.get(id=form.cleaned_data['site_id'])
			user_profile.save()

			return HttpResponseRedirect(reverse('users:profile', kwargs={'user_id': user.id}))
	else:
		default_data = {'first_name': user.first_name, 'last_name': user.last_name,'short_number': user_profile.short_number, 'phone_number': user_profile.phone_number,'experience':user_profile.experience, 'education':user_profile.education,'skill':user_profile.skill,'job':user_profile.job }
		form = ProfileForm(default_data)
	return render(request, 'users/profile.html', {'form': form, 'user': user})


def register(request):
	if request.method == 'POST':

		form = RegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password2']

			# 使用内置User自带create_user方法创建用户，不需要使用save()
			user = User.objects.create_user(username=username, password=password, email=email)

			# 如果直接使用objects.create()方法后不需要使用save()
			user_profile = UserProfile(user=user)
			user_profile.save()

			return HttpResponseRedirect("/accounts/login/")

	else:
		form = RegistrationForm()

	return render(request, 'users/registration.html', {'form': form})


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = auth.authenticate(username=username, password=password)

			if user is not None and user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect(reverse('users:profile', kwargs={'user_id': user.id}))

			else:
				# 登陆失败
				return render(request, 'users/login.html', {'form': form, 'message': 'Wrong password. Please try again.'})
	else:
		form = LoginForm()
	return render(request, 'users/login.html', {'form': form})
