from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('counseling/', include('counseling_app.urls')),
    path('about/', include('about_app.urls')),
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # robots.txt
    path("robots.txt",
        TemplateView.as_view(template_name="robots.txt",
                              content_type="text/plain"),
    ),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)