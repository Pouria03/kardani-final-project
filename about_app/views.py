from django.shortcuts import render
from django.views import View
from .services import (get_data_about_company,
                       get_frequent_questions)

# Create your views here.
class AboutCompanyView(View):
    """
        In respond to requests for
        this view, get the data about
        company and boss and also frequent
        asked questions from models
        AboutCompany and FrequentQuestion
    """
    def get(self, request):
        about_company = get_data_about_company()
        frequent_questions = get_frequent_questions()

        context = {
            'about_company' : about_company,
            'frequent_questions' : frequent_questions
        }

        return render(request, None, context)