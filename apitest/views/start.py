from django.shortcuts import render, redirect, HttpResponse
from apitest import models
from apitest.form.allform import StartModelForm, EnvModelForm
from apitest.views.process_request import Process_method
import json


def start_test(request):
    if request.method == 'GET':
        form = StartModelForm()
        return render(request, 'start.html', {'form': form})
    env_form = StartModelForm(request.POST)

    if env_form.is_valid():
        env_nid = env_form.cleaned_data['hosts']
        api_nid = env_form.cleaned_data['api']
        print(env_nid)
        print(api_nid)
        env_queryset = models.RunEnv.objects.filter(id=env_nid).first()
        envlist = [env_queryset.host, env_queryset.token, env_queryset.appkey]
        if len(api_nid) == 1:
            api_queryset = models.ApiManage.objects.filter(id=api_nid[0]).first()
            apilist = [api_queryset.apiname, api_queryset.url, api_queryset.header, api_queryset.parmary,
                       api_queryset.body, api_queryset.methor]
            if api_queryset.parmary == None:
                apilist.remove(api_queryset.parmary)
            elif api_queryset.body == None:
                apilist.remove(api_queryset.body)
            print('env: ',envlist,apilist)
            orgname = env_queryset.appkey.split('#')[0]
            appname = env_queryset.appkey.split('#')[1]
            print('appkey:',orgname,appname)
            header = json.loads(api_queryset.header % (env_queryset.token))
            print('header:',header,type(header))
            #实例化处理请求的类
            run_test = Process_method(env_queryset.host,orgname,appname,header)
            #将参数转换成dict
            parmary = json.loads(api_queryset.parmary)

            if api_queryset.parmary != None:
                url = api_queryset.url.urlname % (parmary['url'])
                print(url)
            else:
                url = api_queryset.url
            if api_queryset.methor == 1:
                    run_test.process_post(url,api_queryset.body)
            if api_queryset.methor == 2:
                    code,result = run_test.process_get(url)
            print('result: ',code,result)
            term = models.Test_Result.objects.filter(api=api_queryset.apiname).first()
            if term:
                models.Test_Result.objects.update(api=api_queryset.apiname,
                                                status_code=code,
                                                test_content=result)
            else:
                models.Test_Result.objects.create(api=api_queryset.apiname,
                                                  status_code=code,
                                                  test_content=result)
            return HttpResponse('状态码：%s,结果：%s' %(code,result))

    return render(request, 'start.html', {'form': env_form})
