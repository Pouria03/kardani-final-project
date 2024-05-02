from django.test import TestCase
from ..models import (BoldCustomer,
                      CompanyAttribute,
                      CompanyService,
                      IndexPage)


class TestBoldCustomer(TestCase):

    def test_bold_customer_str_method(self):
        bold_customer = BoldCustomer.objects.create(name='test bold customer')
        self.assertEqual(str(bold_customer), 'test bold customer')


class TestCompanyAttribute(TestCase):

    def test_company_attribute_str_method(self):
        company_attribute = CompanyAttribute.objects.create(title='something')
        self.assertEqual(str(company_attribute), 'something')


class TestCompanyService(TestCase):

    def test_company_service_str_method(self):
        company_service = CompanyService.objects.create(service_title='test company service')
        self.assertEqual(str(company_service), 'test company service')


class TestIndexPage(TestCase):

    def test_index_page_str_method(self):
        index_page = IndexPage.objects.create(intro_title='test index page')
        self.assertEqual(str(index_page), 'test index page')