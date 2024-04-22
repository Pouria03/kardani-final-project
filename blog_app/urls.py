from django.urls import path
from views import (PostDetailView,
                   PostListView)

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<id:int>/', PostDetailView.as_view(), name='post_detail')
]