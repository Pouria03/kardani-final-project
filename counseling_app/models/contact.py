from django.db import models
from counseling_app.models import Counseling



class Contact(models.Model):
    name = models.CharField(max_length=60,
                            verbose_name='نام',
                            help_text='نام کسی که فرم ثبت درخواست'\
                            '  در صفحه مشاوره را ثبت کرده است'  
    )
    
    counseling_type = models.ForeignKey(Counseling,
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        verbose_name='نوع مشاوره درخواستی',
                                        help_text='نوع مشاوره ای که کاربر در فرمی'\
                                        ' که در صفحه مشاوره است ثبت کرده. '
    )

    user_phone = models.CharField(max_length=11,
                                  verbose_name='موبایل کاربر')
    
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='تاریخ ثبت فرم درخواست')

    def __str__(self) -> str:
        return self.name + ' - ' + self.counseling_type.title
    
    class Meta:
        verbose_name = ' فرم ثبت درخواست های کاربر'
        verbose_name_plural = 'فرم های ثبت درخواست کاربران'