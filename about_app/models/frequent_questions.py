from django.db import models



class FrequentQuestion(models.Model):
    question = models.TextField(max_length=500,
                                unique=True)
    
    answer = models.TextField(max_length=1500)

    def __str__(self) -> str:
        return self.question[:15] + '...'