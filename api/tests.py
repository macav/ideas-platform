import json

from django.contrib.auth import get_user_model
from django.test import TestCase, Client


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
