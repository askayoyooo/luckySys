from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
import re
from users import models

NUM_LETTER = re.compile("^(?!\d+$)[\da-zA-Z_]+$")  # 数字和字母组合，不允许纯数字
FIRST_LETTER = re.compile("^[a-zA-Z\d]")  # 只能以字母开头


def account_name_fomart(Name):
	if NUM_LETTER.search(Name):
		if FIRST_LETTER.search(Name):
			return True
	return False


def email_check(email):
	pattern = re.compile(r"\"?([-_a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
	return re.match(pattern, email)


class RegistrationForm(forms.Form):

	# username = forms.CharField(label='Username', max_length=50)
	# email = forms.EmailField(label='Email',)
	# password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	# password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
	username = forms.CharField(max_length=50)
	email = forms.EmailField()
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	# Use clean methods to define custom validation rules

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if not account_name_fomart(username):
			raise forms.ValidationError("Your UserID must be at least 6 characters long.")
		elif len(username) < 6:
			raise forms.ValidationError("Your UserID must be at least 6 characters long.")
		elif len(username) > 50:
			raise forms.ValidationError("Your UserID is too long.")
		else:
			filter_result = User.objects.filter(username__exact=username)
			if len(filter_result) > 0:
				raise forms.ValidationError("Your UserID already exists.")

		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')

		if email_check(email):
			filter_result = User.objects.filter(email__exact=email)
			if len(filter_result) > 0:
				raise forms.ValidationError("Your email already exists.")
		else:
			raise forms.ValidationError("Please enter a valid email.")

		return email

	def clean_password1(self):
		password1 = self.cleaned_data.get('password1')

		if len(password1) < 6:
			raise forms.ValidationError("Your password is too short.")
		elif len(password1) > 20:
			raise forms.ValidationError("Your password is too long.")

		return password1

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Password mismatch. Please enter again.")

		return password2


class LoginForm(forms.Form):

	username = forms.CharField(label='Username', max_length=50)
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	# Use clean methods to define custom validation rules

	def clean_username(self):
		username = self.cleaned_data.get('username')

		if email_check(username):
			filter_result = User.objects.filter(email__exact=username)
			if not filter_result:
				raise forms.ValidationError("This email does not exist.")
		else:
			filter_result = User.objects.filter(username__exact=username)
			if not filter_result:
				raise forms.ValidationError("This username does not exist. Please register first.")

		return username


class ProfileForm(forms.Form):

	first_name = forms.CharField(label='First Name', max_length=50, required=False)
	last_name = forms.CharField(label='Last Name', max_length=50, required=False)
	short_number = forms.CharField(label='Short Number', max_length=50, required=False)
	phone_number = forms.CharField(label='Phone Number', max_length=50, required=False)
	experience = forms.CharField(widget=forms.Textarea, label='Experience', max_length=500, required=False)
	skill = forms.CharField(label='Skill',max_length=200, required=False)
	education = forms.CharField(label='Education',max_length=128, required=False)
	job = forms.CharField(label="Job", max_length=64, required=False)
	site_id = forms.fields.IntegerField(widget=widgets.Select(choices=models.Site.objects.values_list('id', 'name'),))
	avatar = forms.ImageField(label='Avatar', required=False)


class PwdChangeForm(forms.Form):
	old_password = forms.CharField(label='Old password', widget=forms.PasswordInput)

	password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

	# Use clean methods to define custom validation rules

	def clean_password1(self):
		password1 = self.cleaned_data.get('password1')

		if len(password1) < 6:
			raise forms.ValidationError("Your password is too short.")
		elif len(password1) > 20:
			raise forms.ValidationError("Your password is too long.")

		return password1

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')

		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Password mismatch. Please enter again.")
