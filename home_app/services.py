from home_app.models import (CompanyAttribute,
                             CompanyInfo,
                             CompanyService,
                             Customer)



def get_all_company_services():
    return CompanyService.objects.all()


def get_all_customers():
    return Customer.objects.all()


def get_company_info():
    try:
        return CompanyInfo.objects.first()
    except :
        raise ValueError('object not found')
    

def get_company_attributes():
    return CompanyAttribute.objects.all()