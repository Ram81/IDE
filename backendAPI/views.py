# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.http import JsonResponse


# Create your views here.
class login(TemplateView):
    template_name = 'login.html'


def check_login(request):
    return JsonResponse({'result': request.user.is_authenticated()})
