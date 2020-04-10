import os

from django.contrib.auth.models import User
from django.urls import reverse
from locust import HttpLocust, TaskSet, task, between
from django.utils.crypto import get_random_string
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import django
django.setup()

# locust -f api/tests/locust.py --no-web -c 10000 -r 100

class WebsiteTasks(TaskSet):
    def setUp(self):
        self.username = get_random_string(5)
        self.password = get_random_string(15)
        self.email = get_random_string(8)+'@'+get_random_string(8)+'.com'
        self.data = {
            'username': self.username,
            'password': self.password,
            'email': self.email
        }

    def test_can_create_superuser(self):
        user = User.objects.create_user(
            username=self.data['username'],
            email=self.data['email'],
            password=self.data['password'])

        return user

    def on_start(self):
        # URL using path name
        url = reverse('token_obtain_pair')
        user = self.test_can_create_superuser()
        # TODO : check for db issues
        # First post to get token
        response = self.client.post(url, self.data, format='json')
        token = response.data['access']
        return token


    @task
    def index(self):
        token = self.on_start()
        # Next get will require the token to connect
        self.client.credentials(HTTP_AxUTHORIZATION='Bearer {0}'.format(token))
        # Next get will require the token to connect
        bearer = 'Bearer {0}'.format(token)
        self.client.credentials(HTTP_AUTHORIZATION=bearer)
        response = self.client.get(reverse('news'))


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)
