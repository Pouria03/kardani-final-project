"""
    This context processor module 
    is responsible to display 
    data of CompanyInfo model in footer
    and parts of pages all over the website
"""

from .services import get_company_info


def company_info(request):
    return {
        'company_info' : get_company_info()
    }