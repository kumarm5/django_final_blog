from django.contrib import admin
from .models import *
from .form import *

# Register your models here.
class TagsAdmin(admin.ModelAdmin):
    fields = (('tag_name','tag_status'),)
    form  = TagForm
    list_display=('tag_name','tag_status')
    search_fields =('tag_name',)
    
admin.site.register(Tags, TagsAdmin)


class BlogAdmin(admin.ModelAdmin):
    fields = (('title', 'post_image'), ('tag', 'user'), ('description'))
    form = BlogForm
    list_display = ('title', 'tag', 'user')
    search_fields = (('title', 'tag'),)

admin.site.register(Blog, BlogAdmin)

