from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .services import (get_counseling,
                        get_all_counselings,
                        submit_user_contact_request)



# Create your views here.
class CounselingDetailView(View):
    """
        Get a counseling object by id and return the object,
        if not found raise 404
    """

    def get(self, request, id):
        counseling = get_counseling(id)
        counseling_types = get_all_counselings()
        return render(request, 'counseling_app/counseling.html',
                      {'counseling': counseling,
                       'counseling_types': counseling_types
                       })


class UserContactFormView(View):
    """
        submiting contact request of
        user for getting counseling services
    """
    def post(self, request):
        form = request.POST
        name=form.get('name')
        phone=form.get('user_phone')
        counseling_type_id=form.get('counseling_type_id')
        if name and phone and counseling_type_id:
            obj = submit_user_contact_request(name=name,
                                            user_phone=phone,
                                            counseling_type_id=counseling_type_id)
            if obj != None:
                messages.success(request, 'فرم شما ثبت شد', extra_tags='success')
                return redirect('counseling_detail', form.get('current_page_url_parameter'))

        messages.success(request, 'نشد. دوباره امتحان کنید', extra_tags='warning')
        return redirect('counseling_detail', form.get('current_page_url_parameter'))
