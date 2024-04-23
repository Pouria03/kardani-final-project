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
    
    def save(self, *args, **kwargs):
        """
            This method is responsible for 
            saving new records for this model.
            in this case, this method let admin
            have the permission to add 
            only one record for this model.
        """
        # Check if a record already exists
        if self.__class__.objects.exists():
            raise ValueError("A record with this email already exists.")
        
        # If not, proceed with saving the record
        super().save(*args, **kwargs)
