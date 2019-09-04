from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	# username = models.CharField(max_length=32, blank=True, null=True) // User 的first name/ last name
	# job_number = models.CharField(max_length=32, unique=True) // User 的user name
	# email = models.CharField(max_length=64, blank=True, null=True)// User email
	short_number = models.CharField(max_length=32,blank=True, null=True)
	phone_number = models.CharField(max_length=64, blank=True, null=True)
	experience = models.TextField(max_length=500, blank=True, null=True)
	skill = models.CharField(max_length=200, blank=True, null=True)
	education = models.CharField(max_length=128, blank=True, null=True)
	job = models.CharField(max_length=64, blank=True, null=True)
	avatar = models.ImageField(upload_to='avatar')
	site = models.ForeignKey("Site", on_delete=models.CASCADE, blank=True, null=True)

	class Meta:
			verbose_name='User Profile'

	def __str__(self):
		return self.user.__str__()


class Site(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True)

	def __str__(self):
		return self.name

