from django.db import models


# Create your models here.


class UrlManage(models.Model):
    """
    url管理
    """
    urlname = models.CharField(verbose_name='url名称',max_length=128)
    func = models.CharField(verbose_name='类别名称',max_length=32)
    def __str__(self):
        return self.urlname


class ApiManage(models.Model):
    '''
    Api管理
    '''
    apiname = models.CharField(verbose_name='接口功能',max_length=32,unique=True)
    url = models.ForeignKey(verbose_name='url地址',to=UrlManage)
    header = models.CharField(verbose_name='请求头',max_length=128)
    parmary = models.CharField(verbose_name='url参数',max_length=64,null=True,blank=True)
    body = models.CharField(verbose_name='请求body',max_length=1024,null=True,blank=True)
    methor_choices = (
        (1, 'POST'),
        (2, 'GET'),
        (3, 'PUT'),
        (4, 'DELETE'),
    )
    methor = models.IntegerField(verbose_name='请求方法',choices=methor_choices)

    def __str__(self):
        return self.apiname


class RunEnv(models.Model):
    """
    运行环境
    """
    host = models.CharField(verbose_name='主机环境',max_length=32,unique=True)
    token = models.CharField(verbose_name='管理员帐号',max_length=512)
    appkey = models.CharField(verbose_name='appkey名称',max_length=32)
    def __str__(self):
        return self.host


class Test_Result(models.Model):
    """
    测试结果
    """
    api = models.CharField(verbose_name='功能接口',max_length=32,unique=True)
    status_code = models.CharField(verbose_name='返回的状态码',max_length=16)
    test_content = models.TextField(verbose_name='测试结果')
    test_data = models.DateTimeField(verbose_name='最后执行时间',auto_now=True)
