from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .services import get_counseling
from .forms import UserContactForm


# Create your views here.
class CounselingDetailView(View):
    """
        Get a counseling object by id and return the object,
        if not found raise 404
    """
    def get(self, request, id):
        counseling = get_counseling(id)
        return render(request, None, {'counseling':counseling})
    

# TODO: complete contact view's security
class UserContactFormView(View):
    """
        Displaying and submiting
        contact request of user
        for getting counseling services
    """

    form_class = UserContactForm
    def get(self, request):
        form = self.form_class()
        return render(request, None, {'form':form})

    def post(self, request):
        form = self.form_class(data=request.data)
        if form.is_valid():
            form.save()
            messages.success(request, 'فرم شما ثبت شد')
            return redirect('/')