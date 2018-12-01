from django.shortcuts import render,redirect
from apitest import models
from apitest.form.allform import UrlModelForm
from django.urls import reverse

def urlslist(request):
    url_queryset = models.UrlManage.objects.all()
    return render(request, 'urlslist.html', {'url_queryset':url_queryset})


def urladd(request):
    """
    增加Url
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = UrlModelForm()
        return render(request,'change.html',{'form':form})
    form = UrlModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('urllist'))
    return render(request,'change.html',{'form':form})


def urledit(request,nid):
    """
    编辑Url
    :param request:
    :return:
    """
    obj = models.UrlManage.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UrlModelForm(instance=obj)
        return render(request,'change.html',{'form':form})
    form = UrlModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('urllist'))
    return render(request,'change.html',{'form':form})


def urldel(request,nid):
    origin = reverse('urllist')
    if request.method == 'GET':
        return render(request,'delete.html',{'cancel':origin})
    models.UrlManage.objects.filter(id=nid).delete()
    return redirect(origin)

