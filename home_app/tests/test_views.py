from django.test import TestCase, Client
from django.urls import reverse

class IndexPageTestCase(TestCase):
    """
        Test indexpage view
    """
    def setUp(self):
        self.client = Client()

    def test_get_request(self):
        """
            Test if the get request 
            returns ok.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """
            Test if the template indexPage view
            uses is correct.
        """
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'home_app/index.html')

    def test_context_data(self):
        """
            Test if the data passed
            to context is as expected.
        """
        response = self.client.get(reverse('index'))
        self.assertIn('company_services', response.context)
        self.assertIn('bold_customers', response.context)
        self.assertIn('intro_data', response.context)
        self.assertIn('company_attrs', response.context)