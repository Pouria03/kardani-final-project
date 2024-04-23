from django.db import models



class CompanyService(models.Model):
    """
        This model is responsible to store 
        and display services that this comapny
        presents.
    """

    service_title = models.CharField(max_length=75, unique=True,
                                     verbose_name='عنوان خدمت (سرویس)',
                                     help_text="عنوان خدمتی که رائه میکنید را وارد کنید")
    icon_svg_code = models.CharField(max_length=1000,
                                      help_text="یک کد svg را درون این باکس قرار دهید")

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'خدمات/سرویس ها'
        verbose_name_plural = 'خدمات/سرویس ها'
    