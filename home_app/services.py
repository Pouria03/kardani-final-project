"""
    services.py is here to seperate
    business logic from views and models.
"""

from home_app.models import (CompanyAttribute,
                             IndexPage,
                             CompanyService,
                             BoldCustomer)



def get_all_company_services() -> list:
    """This function returns
    list of CompanyService objects.
    """
    return CompanyService.objects.all()


def get_all_bold_customers() -> list:
    """This function returns
    list of BoldCustomer objects.
    """
    return BoldCustomer.objects.all()


def get_index_page_data():
    """This function returns first 
    object of IndexPage object."""
    try:
        return IndexPage.objects.first()
    except IndexPage.DoesNotExist:
        return None
    
    
def get_company_attributes() -> list:
    """This function returns a list
    of CompanyAttribute objects."""
    return CompanyAttribute.objects.all()