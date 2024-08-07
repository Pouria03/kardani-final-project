from django.shortcuts import render
from django.views import View
from .services import (get_all_company_services,
                       get_all_bold_customers,
                       get_company_attributes,
                       get_index_page_data)



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
            'bold_customers' : get_all_bold_customers(),
            'company_attrs' : get_company_attributes(),
            'intro_data' : get_index_page_data()
        }
        return render(request, 'home_app/index.html', context)