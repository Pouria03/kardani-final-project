from django.urls import path
from .views import (CounselingDetailView,
                    UserContactFormView)

urlpatterns = [
    path('<int:id>/', CounselingDetailView.as_view(), name='counseling_detail'),
    path('request-contact/', UserContactFormView.as_view(), name='contact_request'),
]