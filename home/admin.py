from django.contrib import admin
from .models import Home
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
   list_display = ('id','create_date',)
   list_display_links = ('id','create_date',)
   list_per_page = 25

admin.site.register(Home, HomeAdmin)