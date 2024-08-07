from django.db import models
from ckeditor.fields import RichTextField



class Post(models.Model):
    """
        This model represents table of blog application.
    """
    title = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            verbose_name='عنوان')

    content = RichTextField(blank=False,
                            null=False,
                            verbose_name='متن مطلب')
    
    created_at = models.DateField(auto_now_add=True)

    thumbnail = models.ImageField(upload_to='uploads/thumbnails/',
                                blank=False,
                                null=False,
                                verbose_name='تصویر اصلی مطلب')


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'مطلب'
        verbose_name_plural = 'مطالب'
        ordering = ['-id']