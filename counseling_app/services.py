"""
    services.py is here to seperate
    business logic from views and models.
"""

from .models import Counseling
from .models import Contact
from django.shortcuts import get_object_or_404
import re


def get_all_counselings() -> list:
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
    

def is_phone_number(phone: str) -> bool:
    phone = phone.strip()
    check_phone_regex = re.search(r'^(09)+(\d){9}', phone)
    if check_phone_regex:
        return True

def submit_user_contact_request(**kwargs):
    counsling_type_id : int = int(kwargs['counseling_type_id'])
    if is_phone_number(kwargs['user_phone']):
        return Contact.objects.create(name=kwargs['name'],
                                    user_phone=kwargs['user_phone'],
                                    counseling_type=get_counseling(id=counsling_type_id))
    return None


