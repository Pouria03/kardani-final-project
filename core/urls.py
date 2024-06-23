from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('counseling/', include('counseling_app.urls')),
    path('about/', include('about_app.urls')),
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)