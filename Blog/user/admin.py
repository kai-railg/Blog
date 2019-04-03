import xadmin
# Register your models here.
from user.models import ArticleDetail, Article, Tags


# from django.contrib import admin

class ArticleDetailAdmin(object):
    list_display = ['content', 'tag', 'image', 'create_time', 'update_time']
    search_fields = ['content', 'tag', 'image']
    list_filter = ['content', 'tag', 'image']
    pass


class ArticleAdmin(object):
    list_display = ['title', 'desc', 'image', 'detail', 'create_time', 'update_time']
    pass


class TagsAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    pass


#

xadmin.site.register(ArticleDetail, ArticleDetailAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tags, TagsAdmin)

# admin.site.register(ArticleDetail)
# admin.site.register(Article)
# admin.site.register(Tags)
