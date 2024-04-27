from about_app.models import FrequentQuestion, AboutCompany
from home_app.models import CompanyService


def get_data_about_company():
    """
        This method is responsible for
        getting data and return it 
        for about.html page
    """
    try:
        return AboutCompany.objects.first()
    except AboutCompany.DoesNotExist:
        return None
    

def get_frequent_questions():
    """
        This method is responsible to get
        frequent asked questions and their
        answers (each question have only one answer)
        data is retrieved from model FrequentQuestion
    """

    return FrequentQuestion.objects.all()


def get_services():
    return CompanyService.objects.all()