from django.test import TestCase, Client


class HomepageTestCase(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get("/")

    # def tearDown(self):
    def test_redirect_from_homepage_302_success(self):
        self.assertEqual(self.response_status_code, 302)
        self.assertEqual(self.response.url, reverse("products"))

    def test_open_homepage_200_fail(self):
        self.assertNotEqual(self.response.status_code, 200)
