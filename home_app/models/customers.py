from django.db import models



class Customer(models.Model):
    """
        This model is responsible to store 
        and display bold customers that have
        worked with the company.
    """

    name = models.CharField(max_length=75, unique=True,
                            help_text="نام شرکتی که با شما همکاری کرده است را بنویسید")
    logo = models.ImageField(upload_to='uploads/customer_logos/',
                             help_text="یک تصویر برای لوگوی شرکتی که مشتری شما بوده است انتخاب کنید")


    def __str__(self):
        return self.name