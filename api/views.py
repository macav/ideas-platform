import json

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import ensure_csrf_cookie
from ideas import settings


@method_decorator(ensure_csrf_cookie, name='dispatch')
class IndexView(generic.TemplateView):
    template_name = 'api/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['is_debug'] = settings.DEBUG
        context['ngapp'] = settings.NGAPP
        context['user'] = json.dumps({'id': self.request.user.pk, 'username': self.request.user.username}) if self.request.user.is_authenticated() else None
        context['is_authenticated'] = self.request.user.is_authenticated()
        return context