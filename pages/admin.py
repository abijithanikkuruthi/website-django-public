from django.contrib import admin
from .models import Blog, Message, Tag, Comment, Image

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    list_filter = ['created_on']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'subject', 'send_on')
    list_filter = ['send_on']
    search_fields = ['name', 'subject']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'message')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'id')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Image, ImageAdmin)