from django.contrib import admin
from .models import Team
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
   list_display = ('id','name' ,'email', 'telephone','hire_date','is_mvp',)
   list_display_links = ('id','name')
   list_editable = ('is_mvp',)

admin.site.register(Team, TeamAdmin)
