from django.test import TestCase, Client
from ..models import Post


class PostModelTestCase(TestCase):
    def test_str_method(self):
        """
        Test the __str__ method of the Post model.
        """
        post = Post.objects.create(title='Test Post')
        self.assertEqual(str(post), 'Test Post')