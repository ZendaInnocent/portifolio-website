from django.contrib import admin

from posts.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'status', 'created_on', )
    list_filter = ('status', )
    search_fields = ('title', 'content', )


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active', )
    list_filter = ('created_on', )
    search_fields = ('name', 'email', 'body', )
    actions = ['approve_comments', ]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
