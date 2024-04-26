from django.shortcuts import render
from django.views import View
from .services import (get_all_posts,
                      get_post)

from django.core.paginator import (Paginator,
                                EmptyPage,
                                PageNotAnInteger)


# Create your views here.
class PostListView(View):
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

        return render(request, 'blog_app/blog.html', {'posts': posts})

class PostDetailView(View):
    def get(self, request, id):
        post = get_post(id)
        if post is None:
            raise ValueError('404')
        return render(request, 'blog_app/blog_detail.html', {'post': post})
    