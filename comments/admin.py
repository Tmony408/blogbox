from django.contrib import admin
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
   list_display = ('id','name' ,'email','article_id','comment_date',)
   list_display_links = ('id','name', 'email')
   list_filter = ('article_id','email')

admin.site.register(Comment, CommentAdmin)
