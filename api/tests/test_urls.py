from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class RouteTest(APITestCase):
    def test_news_route_found(self):
        response = self.client.get(reverse('news'))
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_news_no_permission_without_auth_check(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
