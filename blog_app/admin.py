from django.contrib import admin
from blog_app.models import Post





class PostAdmin(admin.ModelAdmin):
    """How to display 
    posts in admin panel is 
    configured here
    """
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', )




# Register your models here.
admin.site.register(Post, PostAdmin)