from django.shortcuts import render
from django.views import View
from services import (get_all_posts,
                      get_post)

# Create your views here.
class PostListView(View):
    def get(self, request):
        posts = get_all_posts()
        # TODO: add template name & add pagination    
        return render(request, '', {'posts': posts})


class PostDetailView(View):
    def get(self, request):
        post = get_post()
        # TODO: add template name
        return render(request, '', {'post': post})