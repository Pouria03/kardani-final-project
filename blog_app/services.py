"""
    services.py is here to seperate
    business logic from views and models.
"""

from .models import Post


def get_all_posts():
    return Post.objects.all()


def get_post(id):
    post = None
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        post = None
    finally:
        return post
    


