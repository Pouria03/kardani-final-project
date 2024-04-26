from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Counseling(models.Model):
    """
        This method represents all counselings that 
        people can recieve from thsis website's owner 
    """
    title = models.CharField(max_length=75, verbose_name='عنوان')

    description = RichTextField(verbose_name='توضیحات')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'مشاوره'
        verbose_name_plural = 'انواع مشاوره ها'