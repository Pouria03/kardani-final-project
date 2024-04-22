from .models import Counseling


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
    try:
        return Counseling.objects.get(id=id)
    except Counseling.DoesNotExist:
        raise ValueError("object not fond")
    
