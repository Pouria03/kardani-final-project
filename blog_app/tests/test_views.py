from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post

class PostListViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_get_request(self):
        """
        Test the response for a GET request.
        """
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """
            Test the correct template is used.
        """
        response = self.client.get(reverse('blog'))
        self.assertTemplateUsed(response, 'blog_app/blog.html')

    def test_context_data(self):
        """
        Test that the correct context data is returned.
        """
        response = self.client.get(reverse('blog'))
        self.assertIn('posts', response.context)
  


class PostDetailViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.post = Post.objects.create(id=9999,
                                        title='title',
                                        content='content',
                                        thumbnail='a.png')

    def test_get_request(self):
        """
        Test the response for a GET request.
        """
        url = reverse('blog_detail', kwargs={'id': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_404_response(self):
        """
        Test the response for a GET request with an invalid id.
        """
        url = reverse('blog_detail', kwargs={'id': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_template_used(self):
        url = reverse('blog_detail', kwargs={'id': 9999})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog_app/blog_detail.html')

    def test_context_data(self):
        """
            Test if data passed
            to context is ok.
        """
        url = reverse('blog_detail', kwargs={'id': 9999})
        response = self.client.get(url)
        self.assertIn('post', response.context)
