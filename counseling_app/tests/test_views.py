from django.test import (TestCase,
                        Client,
                        RequestFactory)
from django.urls import (reverse)
from ..models import Counseling
from django.contrib.messages import get_messages



class CounselingDetailViewTest(TestCase):
    """
        Testing the counseling_detail view
    """
    def setUp(self):
        self.client = Client()
        self.counseling_obj = Counseling.objects.create(id=9999,
                                                        title='title',
                                                        description='desc')

    def test_get_request(self):
        response = self.client.get(reverse('counseling_detail', kwargs={'id': 9999}))
        self.assertEqual(response.status_code, 200)

    def test_context_data(self):
        response = self.client.get(reverse('counseling_detail', kwargs={'id': 9999}))
        self.assertIn('counseling', response.context)
        self.assertIn('counseling_types', response.context)
    

class UserContactFormViewTest(TestCase):
    """
        Testing the user_contact_form view
    """
    def setUp(self):

        self.client = Client()
        self.counseling_obj = Counseling.objects.create(title='title',
                                                        description='desc')

        self.data = {
            'name': 'John Doe',
            'user_phone': '11111111',
            'counseling_type_id': self.counseling_obj.id,
            'current_page_url_parameter': self.counseling_obj.id
        }

    def test_sending_valid_post_request(self):
        """
            Test submiting user's
            contact request with
            valid data.
        """
        response = self.client.post(reverse('contact_request'), self.data)
        all_messages = [msg for msg in get_messages(response.wsgi_request)]
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertEqual(all_messages[0].message, 'فرم شما ثبت شد')


    def test_sending_invalid_post_request(self):
        """
            Test submiting user's
            contact request with
            invalid data.
        """
        invalid_data = self.data.copy()
        invalid_data['name'] = ''
        response = self.client.post(reverse('contact_request'), invalid_data)
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertIn('نشد. دوباره امتحان کنید',
                       [m.message for m in get_messages(response.wsgi_request)])
        

