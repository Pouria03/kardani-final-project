from django.db import models
from home_app.models import HomeBaseModel


class CompanyService(HomeBaseModel):
    """
        This model is responsible to store 
        and display services that this comapny
        presents.
    """
    service_title = models.CharField(max_length=75, unique=True,
                                     verbose_name='عنوان خدمت (سرویس)',
                                     help_text="عنوان خدمتی که رائه میکنید را وارد کنید")
    class Meta:
        verbose_name = 'خدمات/سرویس ها'
        verbose_name_plural = 'خدمات/سرویس ها'
    