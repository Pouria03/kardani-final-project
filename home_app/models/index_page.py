from django.db import models



class IndexPage(models.Model):
    """
        This model stores the info and data about 
        company to present it to its users and customers in 
        the website.
    """

    intro_title = models.CharField(max_length=550, 
                                   verbose_name='عنوان صفحه اصلی وبسایت')

    intro_text = models.TextField(max_length=550,
                                   verbose_name='متن اول صفحه اصلی وبسایت')
    
    intro_video = models.FileField(verbose_name='ویدیوی معرفی صفحه اول وبسایت',
                                   upload_to='uploads/videos/',
                                   blank=True,
                                   null=True)

    def __str__(self) -> str:
        return self.intro_title

    # def save(self, *args, **kwargs):
    #     """
    #         This method is responsible for saving new records.
    #         in this case, this method let admin have the permission
    #         to add only one record for this model.
    #     """
    #     # Check if a record already exists
    #     if self.__class__.objects.exists():
    #         raise ValueError("A record with this email already exists.")
        
    #     # If not, proceed with saving the record
    #     super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'اطلاعات تماس شرکت'
        verbose_name_plural = 'اطلاعات تماس شرکت'