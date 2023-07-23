from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTest(SimpleTestCase):
    def test_url_exists_at_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_home_url_name_available(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)

    def test_home_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    
    def test_home_template_contains(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")



class AboutPageTest(SimpleTestCase):
    def test_url_exists_at_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_url_name_available(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)

    def test_about_template_used(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_about_template_contains(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Page</h1>")