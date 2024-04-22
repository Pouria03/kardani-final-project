from django.urls import path
from .views import CounselingDetailView

urlpatterns = [
    path('<int:id>/', CounselingDetailView.as_view(), name='counseling_detail'),
]