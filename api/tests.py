import json

from api.models import Idea
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APIClient


class TestSessionAuth(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.u = get_user_model().objects.create_user('test1', 'test1@test.com', 'test1password')

    def test_correctly_set_csrf_token(self):
        response = self.client.get('/login/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.client.cookies.get('csrftoken').value, response.context['csrf_token'])

    def test_context_user_not_authenticated(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], None)
        self.assertEqual(response.context['is_authenticated'], False)

    def authenticateUser(self):
        self.client.login(username='test1', password='test1password')

    def test_context_authenticated_user(self):
        self.authenticateUser()
        response = self.client.get('/')
        self.assertEqual(response.context['user'], json.dumps({'id': self.u.pk, 'username': 'test1'}))
        self.assertEqual(response.context['is_authenticated'], True)

    def test_username_in_html(self):
        self.authenticateUser()
        response = self.client.get('/')
        self.assertContains(response, 'test1')

    def test_no_username_in_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'test1')


class TestAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        try:
            self.u = get_user_model().objects.get(pk=1)
        except ObjectDoesNotExist:
            self.u = get_user_model().objects.create_user('test1', 'test1@test.com', 'test1password')
        self.ideas_data = [
            {'title': 'Idea 1', 'content': 'Idea 1 Content', 'user': self.u.pk},
            {'title': 'Idea 2', 'content': 'Idea 2 Content', 'user': self.u.pk},
        ]
        self.ideas = [Idea.objects.create(user=self.u, title='Idea 0', content='Idea 0 Content')]

    def test_should_get_ideas_list(self):
        response = self.client.get('/ideas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'id': self.ideas[0].pk, 'title': 'Idea 0', 'content': 'Idea 0 Content', 'upvotes': 0, 'downvotes': 0, 'user': self.u.pk}])

    def test_should_create_idea(self):
        data = self.ideas_data[0]
        response = self.client.post('/ideas/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(set(data.items()).issubset(set(response.data.items())))
        self.assertEqual(Idea.objects.count(), 2)

    def test_should_not_post_incomplete_idea(self):
        data = self.ideas_data[0]
        del data['user']
        response = self.client.post('/ideas/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
