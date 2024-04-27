from home_app.models import (CompanyAttribute,
                             IndexPage,
                             CompanyService,
                             BoldCustomer)



def get_all_company_services():
    return CompanyService.objects.all()


def get_all_bold_customers():
    return BoldCustomer.objects.all()


def get_index_page_data():
    try:
        return IndexPage.objects.first()
    except IndexPage.DoesNotExist:
        return None
    
    
    

def get_company_attributes():
    return CompanyAttribute.objects.all()