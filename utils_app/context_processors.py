from about_app.models import AboutCompany
from about_app.services import get_data_about_company

def company_info(request):
    return {
        'company_info' : get_data_about_company()
    }