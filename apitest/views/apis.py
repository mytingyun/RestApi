from django.shortcuts import render,redirect
from apitest import models
from django.urls import reverse
from apitest.form.allform import ApiModelForm


def apilist(request):
    api_queryset = models.ApiManage.objects.all()
    return render(request,'apilist.html',{'api_queryset':api_queryset})


def apiadd(request):
    '''
    添加接口
    :param request:
    :return:
    '''
    if request.method == 'GET':
        form = ApiModelForm()
        return render(request,'change.html',{'form':form})
    form = ApiModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('apilist'))
    return render(request,'change.html',{'form':form})

def apiedit(request,nid):
    """
    编辑接口
    :param request:
    :return:
    """
    obj = models.ApiManage.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = ApiModelForm(instance=obj)
        return render(request,'change.html',{'form':form})
    form = ApiModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('apilist'))
    return render(request,'change.html',{'form':form})

def apidel(request,nid):
    origin = reverse('apilist')
    if request.method == 'GET':
        return render(request,'delete.html',{'cancel':origin})
    models.ApiManage.objects.filter(id=nid).delete()
    return redirect(origin)
