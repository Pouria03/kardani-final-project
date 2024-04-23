from django.db import models



class CompanyAttribute(models.Model):
    """
        In this model,
        you can write and add the attributes of
        company that encoureges people to select
        this company's services.
    """

    title = models.CharField(max_length=150,
                              help_text="چرا مشتریان باید خدمات ما را انتخاب کنند؟",
                              verbose_name='خصوصیت شرکت')


    icon_svg_code = models.CharField(max_length=1000,
                                      help_text="یک کد svg را درون این باکس قرار دهید",
                                      verbose_name='آیکون')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'مشتریان چرا باید شرکت ما را انتخاب کنند؟'
        verbose_name_plural = 'مشتریان چرا باید شرکت ما را انتخاب کنند؟'