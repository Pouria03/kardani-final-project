from django.shortcuts import render
from django.views import View
from .services import (get_all_posts,
                      get_post,
                      search_in_posts)

from django.core.paginator import (Paginator,
                                EmptyPage,
                                PageNotAnInteger)


class PostListView(View):
    """This class based view
    returns the list of posts
    in each request.
    """
    def get(self, request):
        posts = get_all_posts()
        paginator = Paginator(posts, 6) # 10 posts per page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, 'blog_app/blog.html',
                       {'posts': posts})
    

class PostSearchView(View):
    """This class based view
    has one get method and returns 
    the result of search in Post objects
    """
    def get(self, request):
        q = request.GET.get('search-input')
        posts = search_in_posts(q)
        posts_count = len(posts)
        return render(request, 'blog_app/blog_search_result.html',
                      {'posts':posts, 'posts_count': posts_count})


class PostDetailView(View):
    """This class based view
    has a get method and takes
    id as its only arguement and
    returns one Post object if exists.
    """
    def get(self, request, id: int):
        post = get_post(id)
        if post is None:
            raise ValueError('404')
        return render(request, 'blog_app/blog_detail.html', 
                      {'post': post})
    