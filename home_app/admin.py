from django.contrib import admin
from home_app.models import (CompanyAttribute,
                             IndexPage,
                             CompanyService,
                             BoldCustomer)



class IndexPageAdmin(admin.ModelAdmin):
    """
        This class is going to remove 
        add button and remove button from 
        model CompanyInfo in admin panel
    """
    list_display = ('intro_title', )

    # if any object has been created in 'AbouCompany' model, remove 'add new' button from admin panel
    # if IndexPage.objects.exists():
    #     def has_add_permission(self, request):
    #         return False

    # def has_delete_permission(self, request, obj=None) -> bool:
    #     return False


# Register your models here.
admin.site.register(CompanyAttribute)
admin.site.register(IndexPage, IndexPageAdmin)
admin.site.register(CompanyService)
admin.site.register(BoldCustomer)
