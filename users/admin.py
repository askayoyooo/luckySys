from django.contrib import admin
from users import models
# Register your models here.


class ActivityAdmin(admin.ModelAdmin):
	list_display = ('name',)


admin.site.register(models.Activity, ActivityAdmin)
