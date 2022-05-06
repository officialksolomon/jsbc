from django.urls import resolve, reverse
from django.test import TestCase

from main.views import HomepageView

# Create your tests here.


class HomepageTestCase(TestCase):
    #
    def test_homepage_url_response_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        #

    def test_root_url_resolves_to_hompage(self):
        result = resolve('/')
        self.assertEqual(result.func.view_class, HomepageView)
