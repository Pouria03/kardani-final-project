from django.contrib import admin
from counseling_app.models import (Contact,
                                   Counseling)




class ContactAdmin(admin.ModelAdmin):
    """
        modifying admin panel of 
        contacts that people made
        from contact form in counseling web page.
    """
    list_display = ('name', 'counseling_type', 'user_phone', 'created_at')
    search_fields = ('name', 'counseling_type', 'user_phone')
    list_filter = ('created_at', 'counseling_type')



class CounselingAdmin(admin.ModelAdmin):
    """
        modyfing admin panel of
        counsel and mentoring services.
    """
    list_display = ('title', 'description')
    search_fields = ('title', 'description')



# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Counseling, CounselingAdmin)
