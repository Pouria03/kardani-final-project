from django.db import models
from ckeditor.fields import RichTextField



class FrequentQuestion(models.Model):
    question = models.TextField(max_length=500,
                                verbose_name='پرسش')
    
    answer = RichTextField(max_length=1500,
                              verbose_name='پاسخ')

    def __str__(self) -> str:
        return self.question[:15] + '...'
    

    class Meta:
        verbose_name = 'پرسش های پرتکرار'
        verbose_name_plural = 'پرسش های پرتکرار'