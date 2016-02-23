from django.conf.urls import url
from ideas import settings

from . import views
from django.contrib.auth import views as auth_views

template_name = {'template_name': 'api/login.html',
                 'extra_context': {'is_debug': settings.DEBUG},
                }

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', auth_views.login, template_name, name='login'),
    url(r'^logout/$', auth_views.logout, template_name, name='logout'),
]

if not settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], serve, {'document_root': settings.DIST_ROOT}),
    ]