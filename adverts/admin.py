from django.contrib import admin
from .models import Advert
# Register your models here.
class AdvertAdmin(admin.ModelAdmin):
   list_display = ('id', 'add_date',)
   list_display_links = ('id', 'add_date',)
   list_per_page = 25

admin.site.register(Advert, AdvertAdmin)