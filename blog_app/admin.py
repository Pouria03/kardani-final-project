from django.contrib import admin
from blog_app.models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', )



# Register your models here.
admin.site.register(Post, PostAdmin)