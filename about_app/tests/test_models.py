"""
    This test modlue is
    for testing models
    of about_app's models
"""

from django.test import TestCase
from ..models import (AboutCompany, 
                    FrequentQuestion)

class AboutCompanyModelTestCase(TestCase):
    """
    Test case for the AboutCompany model.
    """

    def test_str_method(self):
        """
        Test the __str__ method.
        """
        about_company = AboutCompany.objects.create(comapny_name='Test name')
        self.assertEqual(str(about_company), 'Test name')


class FrequentQuestionModelTestCase(TestCase):
    """
    Test case for the FrequentQuestion model.
    """

    def test_str_method(self):
        """
        Test the __str__ method.
        """
        frequent_q = FrequentQuestion.objects.create(question='Test Post')
        self.assertEqual(str(frequent_q), frequent_q.question[:15]+'...')