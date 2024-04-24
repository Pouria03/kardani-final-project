from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Counseling(models.Model):
    """
        This method represents all counselings that 
        people can recieve from thsis website's owner 
    """
    title = models.CharField(max_length=75)

    description = CKEditor5Field(config_name='extends')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'مشاوره'
        verbose_name_plural = 'انواع مشاوره ها'