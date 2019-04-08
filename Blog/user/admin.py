# Register your models here.
from user.models import ArticleDetail, Article, Tags, Filter
from django.contrib import admin

class ArticleDetailAdmin(admin.ModelAdmin):
    list_display = ['content', 'image', 'create_time', 'update_time']
    search_fields = ['content', 'image']
    list_filter = ['content', 'image']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'image', 'detail', 'tag', 'tag_filter',
                    'position', 'create_time', 'update_time']


class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class FilterAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(ArticleDetail, ArticleDetailAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Filter, FilterAdmin)
