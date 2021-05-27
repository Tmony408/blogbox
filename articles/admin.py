from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
   list_display = ('id', 'title', 'topic','is_published','post_date','reporter')
   list_display_links = ('id','topic','title',)
   list_filter = ('reporter','title')
   
   search_fields = ('city', 'title', 'description','topic',)
   list_per_page = 25

admin.site.register(Article, ArticleAdmin)
