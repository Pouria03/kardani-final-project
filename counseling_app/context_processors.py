from .services import get_all_counselings

def counseling_types(request) -> list:
    """
    This context proessor is to display list of 
    counseling types in the header of website
    in all pages.
    """
    return {
            'counseling_types':  get_all_counselings()
    }