from django.contrib import admin
from django.http import HttpRequest
from .models import (FrequentQuestion
                     , AboutCompany)


class FrequentQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', )
    search_fields = ('question', 'answer')


class AboutCompanyAdmin(admin.ModelAdmin):
    """
        This class is going to remove 
        add button and remove button from 
        model AboutCompany in admin panel
    """
    list_display = ('comapny_name', )


#     # if any object has been created in 'AbouCompany' model, remove 'add new' button from admin panel
    if AboutCompany.objects.exists():
        def has_add_permission(self, request):
            return False
        
    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    


# # Register your models here.
admin.site.register(FrequentQuestion,
                     FrequentQuestionAdmin)

admin.site.register(AboutCompany,
                    AboutCompanyAdmin)