from django.shortcuts import render
from django.views import View
from .services import (get_all_company_services,
                       get_all_bold_customers,
                       get_company_attributes,
                       get_company_info)


# Create your views here.
class IndexView(View):
    """
        This view represents for displaying 
        data and introducing company
        and it is the home (main) page of
        the website.
    """
    def get(self, request):
        context = {
            'company_services' : get_all_company_services(),
            'customers' : get_all_bold_customers(),
            'company_attrs' : get_company_attributes(),
            'comapny_general_info' : get_company_info()
        }
        return render(request, 'home_app/index.html', context)