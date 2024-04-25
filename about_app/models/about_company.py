from django.db import models



class AboutCompany(models.Model):
    comapny_name = models.CharField(max_length=75,
                                    verbose_name='نام شرکت')

    description_about_company = models.TextField(max_length=1500,
                                                 verbose_name='درباره شرکت')

    boss_name = models.CharField(max_length=75,
                                 verbose_name='نام و نام خانوادگی رییس ')
    
    description_about_boss = models.TextField(max_length=1500,
                                              verbose_name='درباره رییس شرکت')

    picture_about_boss = models.ImageField(upload_to='uploads/customer_logos/',
                                           verbose_name='تصویر مالک یا رییس شرکت')
    

    def __str__(self):
        return self.comapny_name
    


    class Meta:
        verbose_name = 'توضیحات درباره شرکت و رئیس'
        verbose_name_plural = 'توضیحات درباره شرکت و رئیس'