from django.shortcuts import render,redirect
from apitest import models
from apitest.form.allform import EnvModelForm
from django.urls import reverse


def envlist(request):
    env_queryset = models.RunEnv.objects.all()
    return render(request,'envlist.html',{'env_queryset':env_queryset})


def envadd(request):
    """
    添加集群环境
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = EnvModelForm()
        return render(request,'change.html',{'form':form})
    form = EnvModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('envlist'))
    return render(request,'change.html',{'form':form})


def envedit(request,nid):
    """
    编辑集群环境
    :param request:
    :return:
    """
    obj = models.RunEnv.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = EnvModelForm(instance=obj)
        return render(request,'change.html',{'form':form})
    form = EnvModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('envlist'))
    return render(request,'change.html',{'form':form})


def envdel(request,nid):
    origin = reverse('envlist')
    if request.method == 'GET':
        return render(request,'delete.html',{'cancel':origin})
    models.RunEnv.objects.filter(id=nid).delete()
    return redirect(origin)
