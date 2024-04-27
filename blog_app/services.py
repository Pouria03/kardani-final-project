"""
    services.py is here to seperate
    business logic from views and models.
"""

from .models import Post
from django.shortcuts import get_object_or_404


def get_all_posts():
    return Post.objects.all().only('title', 'thumbnail', 'created_at')


def get_post(id):
    return get_object_or_404(Post, id=id)
    


