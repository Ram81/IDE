# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.models import User


# Create your views here.
class login(TemplateView):
    template_name = 'login.html'


def check_login(request):
    try:
        user = User.objects.get(username=request.user.username)
        user_id = user.id
        username = ''

        is_authenticated = user.is_authenticated()
        if (is_authenticated):
            username = user.username

        return JsonResponse({
            'result': is_authenticated,
            'user_id': user_id,
            'username': username
        })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'error': str(e)
        })
