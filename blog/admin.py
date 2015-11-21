from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'favourite')
    list_filter = ('favourite',)
    search_fields = ('title', 'id')

admin.site.register(Post, PostAdmin)