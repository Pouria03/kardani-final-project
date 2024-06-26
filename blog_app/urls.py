from django.urls import path, re_path
from .views import (PostDetailView,
                   PostListView,
                   PostSearchView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('<int:id>/', PostDetailView.as_view(), name='blog_detail'),
    path('search/', PostSearchView.as_view(), name='search'),
        # re_path('^(search/){1}$', PostSearchView.as_view(), name='search')

]