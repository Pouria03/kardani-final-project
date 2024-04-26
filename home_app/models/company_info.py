from django.db import models



class CompanyInfo(models.Model):
    """
        This model stores the info and data about 
        company to present it to its users and customers in 
        the website.
    """

    company_name = models.CharField(max_length=100,
                                    verbose_name='نام شرکت')

    email = models.EmailField(unique=True,
                              verbose_name="ایمیل شرکت")
    
    phone = models.CharField(max_length=11,
                              verbose_name="موبایل شرکت")
    
    tel = models.CharField(max_length=11,
                            verbose_name="تلفن شرکت")

    about_company = models.TextField(max_length=1000,
                                      verbose_name="توضیح و معرفی شرکت")
    
    office_addres = models.CharField(max_length=500,
                                      verbose_name="ادرس محل دفتر")
    
    intro_video = models.FileField(verbose_name='ویدیوی معرفی',
                                   upload_to='uploads/videos/',
                                   blank=True,
                                   null=True)
    
    instagram = models.CharField(verbose_name='نام کاربری اکانت اینستاگرام',
                                 max_length=50)
    
    telegram = models.CharField(verbose_name='آی دی کانال یا چت تلگرام',
                                max_length=50)


    def __str__(self) -> str:
        return self.email

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