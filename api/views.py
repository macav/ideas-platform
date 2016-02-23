import json

from api.models import Idea
from api.serializers import IdeaSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import ensure_csrf_cookie
from ideas import settings
from rest_framework import viewsets, status
from rest_framework.response import Response


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


class IdeaList(generics.ListCreateAPIView):
    model = Idea
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Idea
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class IdeaGetMixin():
    def get_object(self, pk):
        try:
            idea = Idea.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None
        return idea


class IdeaUpvote(IdeaGetMixin, generics.GenericAPIView):
    model = Idea
    serializer_class = IdeaSerializer

    def post(self, request, *args, **kwargs):
        idea = self.get_object(kwargs.get('pk'))
        if not idea:
            return Response(status.HTTP_404_NOT_FOUND)
        idea.upvotes += 1
        idea.save()
        return Response(status=status.HTTP_200_OK, data=self.get_serializer(idea).data)


class IdeaDownvote(IdeaGetMixin, generics.RetrieveUpdateDestroyAPIView):
    model = Idea
    serializer_class = IdeaSerializer

    def post(self, request, *args, **kwargs):
        idea = self.get_object(kwargs.get('pk'))
        if not idea:
            return Response(status.HTTP_404_NOT_FOUND)
        idea.downvotes += 1
        idea.save()
        return Response(status=status.HTTP_200_OK, data=self.get_serializer(idea).data)