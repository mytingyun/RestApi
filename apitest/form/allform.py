from django import forms
from apitest import models
from django.forms import ModelForm


class BootStarpModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootStarpModelForm, self).__init__(*args, **kwargs)
        for k, v in self.fields.items():
            v.widget.attrs['class'] = 'form-control'
            v.widget.attrs['placeholder'] = k


class UrlModelForm(BootStarpModelForm):
    class Meta:
        model = models.UrlManage
        fields = '__all__'


class ApiModelForm(BootStarpModelForm):
    class Meta:
        model = models.ApiManage
        fields = '__all__'


class EnvModelForm(BootStarpModelForm):
    class Meta:
        model = models.RunEnv
        fields = '__all__'


class StartModelForm(forms.Form):
    hosts = forms.ChoiceField(label='测试的主机名称', widget=forms.Select(attrs={'class': 'form-control', }))
    api = forms.MultipleChoiceField(label='测试的接口', widget=forms.SelectMultiple(attrs={'class': 'form-control', }))
    test = forms.EmailInput
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hosts'].choices = [(i.pk, i.host) for i in models.RunEnv.objects.all()]
        self.fields['api'].choices = [(i.pk, i.apiname) for i in models.ApiManage.objects.all()]
