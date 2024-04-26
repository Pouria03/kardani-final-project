from .models import Counseling
from .models import Contact
from django.shortcuts import get_object_or_404



def get_all_counselings():
    """
        This method gets all counselings' title
        to display them in header of website.
    """
    return Counseling.objects.all().only('title')

def get_counseling(id: int):
    """
        This method gets a counseling object by id.
        and checks if its found or not.
    """
    return get_object_or_404(Counseling, id=id)
    

def submit_user_contact_request(**kwargs):
    counsling_type_id = int(kwargs['counseling_type'])
    return Contact.objects.create(name=kwargs['name'],
                                  user_phone=kwargs['user_phone'],
                                  counseling_type=get_counseling(id=counsling_type_id))


