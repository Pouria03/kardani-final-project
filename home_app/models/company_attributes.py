from django.db import models
from home_app.models import HomeBaseModel

class CompanyAttribute(HomeBaseModel):
    """
        In this model,
        you can write and add the attributes of
        company that encoureges people to select
        this company's services.
    """

    title = models.CharField(max_length=75, unique=True,
                            verbose_name='عنوان خصوصیت',
                            help_text="یک عنوان بنویسید که چرا مشتری باید این شرکت را انتخاب کند")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مشتریان چرا باید شرکت ما را انتخاب کنند؟'
        verbose_name_plural = 'مشتریان چرا باید شرکت ما را انتخاب کنند؟'