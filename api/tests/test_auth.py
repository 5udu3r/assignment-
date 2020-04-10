from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class AuthTest(APITestCase):
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

        self.assertEqual(user.is_active, 1, 'Active User')
        return user

    def test_go_login_and_get_jwt_token(self):

        # URL using path name
        url = reverse('token_obtain_pair')
        user = self.test_can_create_superuser()
        # TODO : check for db issues
        # First post to get token
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['access']
        return token

    def test_news_permission_via_jwt_token(self):

        token = self.test_go_login_and_get_jwt_token()
        # Next get will require the token to connect
        self.client.credentials(HTTP_AxUTHORIZATION='Bearer {0}'.format(token))
        # Next get will require the token to connect
        bearer = 'Bearer {0}'.format(token)
        self.client.credentials(HTTP_AUTHORIZATION=bearer)
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_search(self):

        token = self.test_go_login_and_get_jwt_token()
        # Next get will require the token to connect
        self.client.credentials(HTTP_AxUTHORIZATION='Bearer {0}'.format(token))
        # Next get will require the token to connect
        bearer = 'Bearer {0}'.format(token)
        self.client.credentials(HTTP_AUTHORIZATION=bearer)
        response = self.client.get(reverse('news'), {'q': 'trump'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
