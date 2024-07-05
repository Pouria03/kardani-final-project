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


    class Meta:
        verbose_name = 'متن اینترو صفحه اصلی'
        verbose_name_plural = 'متن اینترو صفحه اصلی'