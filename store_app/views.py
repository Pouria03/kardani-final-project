from django.shortcuts import render
from django.views import View


# Create your views here.
class StoreView(View):
    def get(self, request):
        return render(request, 'store_app/store.html')