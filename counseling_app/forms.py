from django.forms import ModelForm
from .models import Contact

class UserContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'counseling_type', 'user_phone']
        read_only_fields = ('created_at', )