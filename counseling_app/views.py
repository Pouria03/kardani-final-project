from django.shortcuts import render
from django.views import View
from .services import get_counseling


# Create your views here.
class CounselingDetailView(View):
    """
        Get a counseling object by id and return the object,
        if not found raise 404
    """
    def get(self, request, id):
        counseling = get_counseling(id)
        return render(request, None, {'counseling':counseling})
    

# TODO: complete contact view
class UserContactFormView(View):
    """
        Displaying and submiting
        contact request of user
        for getting counseling services
    """
    def get(self, request):
        ...

    def post(self, request):
        ...
