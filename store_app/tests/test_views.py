from django.test import TestCase, Client
from django.urls import reverse


class StoreViewTestCase(TestCase):
    """
    Test case for the StoreView view.
    """
    def setUp(self):
        client = Client()

    def test_get_request(self):
        """
        Test the response for a GET request.
        """
        url = reverse('store')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    
    def test_template_used(self):
        url = reverse('store')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'store_app/store.html')