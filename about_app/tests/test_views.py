"""
    This test module is for testing 
    about_app app views
"""

from django.test import TestCase, Client
from django.urls import reverse


class AboutCompanyViewTestCase(TestCase):
    """
    Test case for the AboutCompanyView view.
    """

    def setUp(self):
        self.client = Client()

    def test_get_request(self):
        """
        Test the response for a GET request.
        """
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """
        Test that the correct template is used.
        """
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about_app/about.html')

    def test_context_data(self):
        """
        Test that the correct context data is returned.
        """
        response = self.client.get(reverse('about'))
        self.assertIn('about_company', response.context)
        self.assertIn('frequent_questions', response.context)
        self.assertIn('company_services', response.context)
