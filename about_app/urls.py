from django.urls import path
from .views import AboutCompanyView



urlpatterns = [
    path('', AboutCompanyView.as_view(), name='about'),
]