from django.contrib import admin
from home_app.models import (CompanyAttribute,
                             CompanyInfo,
                             CompanyService,
                             BoldCustomer)



class CompanyInfoAdmin(admin.ModelAdmin):
    """
        This class is going to remove 
        add button and remove button from 
        model CompanyInfo in admin panel
    """
    list_display = ('email', 'tel')


    # if any object has been created in 'AbouCompany' model, remove 'add new' button from admin panel
    if CompanyInfo.objects.exists():
        def has_add_permission(self, request):
            return False



# Register your models here.
admin.site.register(CompanyAttribute)
admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(CompanyService)
admin.site.register(BoldCustomer)
