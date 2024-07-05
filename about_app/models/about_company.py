from django.db import models
from ckeditor.fields import RichTextField


class AboutCompany(models.Model):
    comapny_name = models.CharField(max_length=75,
                                    verbose_name='نام شرکت')

    description_about_company = RichTextField(max_length=1500,
                                                 verbose_name='درباره شرکت')

    boss_name = models.CharField(max_length=75,
                                 verbose_name='نام و نام خانوادگی رییس ')
    
    description_about_boss = RichTextField(max_length=1500,
                                              verbose_name='درباره رییس شرکت')

    picture_about_boss = models.ImageField(upload_to='uploads/customer_logos/',
                                           verbose_name='تصویر مالک یا رییس شرکت')
    

    email = models.EmailField(unique=True,
                              verbose_name="ایمیل شرکت")
    
    phone = models.CharField(max_length=11,
                              verbose_name="موبایل شرکت")
    
    tel = models.CharField(max_length=11,
                            verbose_name="تلفن شرکت")
    
    office_addres = models.CharField(max_length=500,
                                      verbose_name="ادرس محل دفتر")
    
    instagram = models.CharField(verbose_name='نام کاربری اکانت اینستاگرام',
                                 max_length=50)
    
    telegram = models.CharField(verbose_name='آی دی کانال یا چت تلگرام',
                                max_length=50)
    

    def __str__(self):
        return self.comapny_name
    


    class Meta:
        verbose_name = 'توضیحات درباره شرکت و رئیس و اطلاعات تماس'
        verbose_name_plural = 'توضیحات درباره شرکت و رئیس و اطلاعات تماس'