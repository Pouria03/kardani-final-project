from django.forms import ModelForm
from .models import Contact

class UserContactForm(ModelForm):
    class meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('created_at', )