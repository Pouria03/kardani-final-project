from django.test import TestCase
from ..models import Contact, Counseling

class ContactModelTestCase(TestCase):
    """
        This is for testing
        Contact model class
    """

    def test_str_method(self):
        """
            This method tests
            __str__ method of Contact
            class
        """
        self.assertEqual(str(Contact(name='test',
                            counseling_type=Counseling.objects.create(title='test'), 
                            user_phone='12345678910')), 'test - test')
        

class CounselingModelTestCase(TestCase):
    """
        This is for testing
        Counseling model class
    """

    def test_str_method(self):
        """
            This method tests
            __str__ method of Counseling
            class
        """
        self.assertEqual(str(Counseling.objects.create(title='test')), 'test')