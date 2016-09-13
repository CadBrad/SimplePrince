from django.contrib import admin
from .models import Registration
from django.http import HttpResponseRedirect

# Register your models here.


class emailadmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email')

    actions = ['get_emails']

    def get_emails (self, request, queryset):
        for obj in queryset:
            response = obj.contact_email + " "
            print response    

admin.site.register(Registration, emailadmin)