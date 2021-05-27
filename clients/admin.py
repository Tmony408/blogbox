from django.contrib import admin
from .models import Client
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
   list_display = ('id','name' ,'company_name','email','testimonial_date',)
   list_display_links = ('id','name', 'email')


admin.site.register(Client, ClientAdmin)
