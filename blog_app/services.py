"""
    services.py is here to seperate
    business logic from views and models.
"""

from .models import Post
from django.db.models import Q
from django.shortcuts import get_object_or_404


def get_all_posts() -> list:
    """Calling this
    function will return
    list of Post objects
    """
    return Post.objects.all().only('title', 'thumbnail', 'created_at')


def get_post(id: int):
    """This function
    takes id as its argument
    and returns one object of Post.
    """
    return get_object_or_404(Post, id=id)
    

def search_in_posts(q: str) -> list:
    """This function
    takes q as its argument 
    and returns a filtered list of Post objects.
    """
    posts = get_all_posts()
    search_result = posts.filter(Q(title__icontains=q)|
                 Q(content__icontains=q))
    
    return search_result
