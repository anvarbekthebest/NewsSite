from django.contrib import admin
from .models import Category, Post, TopPost, Comment




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title', 'slug')
    prepopulated_fields = {"slug": ('title', )}



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    fields = ('title', 'slug', 'image', 'description', 'author', 'category',)
    prepopulated_fields = {"slug": ('title', )}
    list_filter = ('created', 'updated', 'category', 'author', )
    search_fields = ('title', 'slug', 'description', )


class TopPostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', )
    prepopulated_fields = {"slug": ('title', )}
    list_filter = ('created', 'updated', )
    search_fields = ('title', 'slug', 'description', )

admin.site.register(Post, PostAdmin)
admin.site.register(TopPost, TopPostAdmin)
admin.site.register(Comment)
