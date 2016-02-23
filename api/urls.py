from django.conf.urls import url, include
from ideas import settings

from . import views
from django.contrib.auth import views as auth_views

template_name = {'template_name': 'api/login.html',
                 'extra_context': {'is_debug': settings.DEBUG},
                }

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^ideas/$', views.IdeaList.as_view(), name='idea-list'),
    url(r'^ideas/(?P<pk>[0-9]+)$', views.IdeaDetail.as_view(), name='idea-detail'),
    url(r'^ideas/(?P<pk>[0-9]+)/upvote$', views.IdeaUpvote.as_view(), name='idea-upvote'),
    url(r'^ideas/(?P<pk>[0-9]+)/downvote$', views.IdeaDownvote.as_view(), name='idea-downvote'),
    url(r'^login/$', auth_views.login, template_name, name='login'),
    url(r'^logout/$', auth_views.logout, template_name, name='logout'),
]

if not settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], serve, {'document_root': settings.DIST_ROOT}),
    ]