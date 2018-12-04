from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,redirect
from restapi import settings
from django.urls import reverse
import re

class ApiMiddleware(MiddlewareMixin):
    def process_request(self,request):

        print(request.path_info,'222')
        for reg in settings.WHITE_LIST:
            if re.match(reg, request.path_info):
                return None

        permission = request.session.get(settings.LOGIN_SUCCESS_SESSION)
        if not permission:
            return redirect(reverse('login'))
        return None