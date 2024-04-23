from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('counseling/', include('counseling_app.urls')),
    path('about/', include('about_app.urls')),
]
