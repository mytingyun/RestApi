from django.shortcuts import render,redirect
from apitest import models
from django.conf import settings
from django.urls import reverse


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    user_obj = models.User_manage.objects.filter(username=user,password=pwd).first()
    if not user_obj:
        return render(request,'login.html',{'error':'用户名或密码错误'})

    request.session[settings.LOGIN_SUCCESS_SESSION] = 'login success'
    return redirect(reverse('start_test'))

def logout(request):
    request.session.delete()
    return redirect(reverse('login'))