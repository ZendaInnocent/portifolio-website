from django.contrib import admin

from posts.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'status', 'created_on', )
    list_filter = ('status', )
    search_fields = ('title', 'content', )


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
