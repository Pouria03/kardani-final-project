from about_app.models import FrequentQuestion, AboutCompany


def get_data_about_company():
    """
        This method is responsible for
        getting data and return it 
        for about.html page
    """
    data = None
    try:
        data = AboutCompany.objects.first()
    except AboutCompany.DoesNotExist:
        raise ValueError('object not found')
    
    return data


def get_frequent_questions():
    """
        This method is responsible to get
        frequent asked questions and their
        answers (each question have only one answer)
        data is retrieved from model FrequentQuestion
    """

    return FrequentQuestion.objects.all()