from django.urls import resolve, reverse
from django.test import TestCase
from http import HTTPStatus
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


#

# robots.txt tests.......
class RobotsTest(TestCase):
    def test_get(self):
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response["content-type"], "text/plain")
        lines = response.content.decode().splitlines()
        self.assertEqual(lines[0], "User-Agent: *")

    def test_post(self):
        response = self.client.post("/robots.txt")
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)
