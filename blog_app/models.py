from django.db import models


class PostManager(models.Manager):
    ... 

class Post(models.Model):
    """
        This model represents table of blog application.
    """
    title = models.CharField(max_length=50,
                             blank=False,
                             null=False
                             , verbose_name='عنوان')
    
    slug = models.SlugField(unique=True,
                            blank=False,
                            null=False,
                            max_length=100,
                             help_text='نمایش در url مرورگر')
    # TODO: change to ckeditor
    content = models.TextField(max_length=2500,
                               blank=False,
                                null=False)
    
    created_at = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails/',
                                  blank=False,
                                null=False)


    def __str__(self):
        return self.title