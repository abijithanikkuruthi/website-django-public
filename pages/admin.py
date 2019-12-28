from django.contrib import admin
from .models import Blog, Message, Tag

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    list_filter = ['created_on']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'send_on')
    list_filter = ['send_on']
    search_fields = ['name', 'subject']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Tag, TagAdmin)