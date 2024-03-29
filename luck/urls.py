"""luckySys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from luck import views


app_name = 'luck'
urlpatterns = [
    path('', views.index, name='index'),
    path('luckymember', views.lucky_member,name='lucky_member')
    # path('profile/', views.profile, name='profile'),

    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login',),
    # path('logout/', views.logout, name='logout'),
    # path('user/<int:user_id>/profile/', views.profile, name='profile'),
    # path('user/<int:user_id>/profile/update/', views.profile_update, name='profile_update'),
    # path('user/<int:user_id>/pwdchange/', views.pwd_change, name='pwd_change'),

]
