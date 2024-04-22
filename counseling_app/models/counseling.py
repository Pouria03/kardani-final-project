from django.db import models



# Create your models here.
class Counseling(models.Model):
    """
        This method represents all counselings that 
        people can recieve from thsis website's owner 
    """
    title = models.CharField(max_length=75)
    # TODO: add ckeditor to field below
    description = models.TextField(max_length=3000)


    def __str__(self):
        return self.title