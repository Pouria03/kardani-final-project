from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=60)
    # TODO: choose from counseling types
    counseling_type = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.name + ' - ' + self.counseling_type
    
