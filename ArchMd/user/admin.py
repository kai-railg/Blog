from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Article, Category, Tag
from db.admin_bm import BaseOwnerAdmin
from utils.admin_site import custom_site
from .adminform import ArticleAdminForm

# 分类页面可以直接添加文章
class PostInline(admin.TabularInline):
    model = Article
    extra = 4  # 控制额外添加的条数


class TagInline(admin.StackedInline):
    model = Tag
    extra = 4



class CategoryOwnerFilter(admin.SimpleListFilter):
    '''自定义过滤器只展示当前分类'''
    title = '分类过滤器'
    # url 参数的名字，即 ?user_category=id, id从lookups返回的id获取
    parameter_name = 'user_category'

    def lookups(self, request, model_admin):
        ''' 返回要展示的内容和查询用的id '''
        return Category.objects.filter(user=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        ''' 返回列表页数据，
         self.value() 为?owner_category的id'''
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Category)
@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, TagInline]
    list_display = [
        'name', 'status',
        'created_time', 'user', 'post_count']
    fields = ('name', 'status', 'user')

    # 分类下文章的数量
    def post_count(self, obj):
        return obj.article_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag)
@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'created_time', 'user', 'category']
    fields = ('name', 'status', 'user', 'category')


@admin.register(Article)
@admin.register(Article, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = ArticleAdminForm
    list_display = [
        'title', 'category', 'status',
        'tag', 'created_time', 'user', 'operator']

    # fields的高级版，控制编辑页面的布局，通过元组分成一段一段
    fieldsets = (
        # 每一段的头信息，样式中的文本
        ('基础配置', {
            # 附栏信息，相当于段的描述 -> p标签
            'description': '基础配置描述',
            # 字段信息，放在一个元组里表示同行显示
            'fields': (('title', 'category'), 'status'),
        }),
        ('内容', {
            'fields': ('desc', 'tag', 'content'),
        }),
        ('额外信息', {
            # 控制是否显示，当前为隐藏，可选显示；
            # wide 为显示，默认支持两个字段，可以自己写并配置相应的 css文件
            'classes': ('collapse',),
            'fields': ('user',),
        })
    )
    # 横向和纵向展示，字段需要是 多对多字段类型
    # filter_horizontal = ('tags',)
    # filter_vertical = ('tags', )

    # 作为链接的字段
    list_display_links = []

    # 过滤字段
    # list_filter = ['category']
    # 使用自定义的过滤类, 用户只能看到自己的过滤内容
    list_filter = [CategoryOwnerFilter]

    # 搜索字段
    search_fields = ['title', 'category__name', 'tag__name']
    # 动作相关的配置，是否展示在顶部
    actions_on_top = True
    # 动作相关的配置，是否展示在底部
    actions_on_bottom = True

    # 保存、编辑、编辑并新建 按钮是否在顶部展示
    save_on_top = True

    # 自定义函数的参数是当前行的对象，
    def operator(self, obj):
        # 返回 html 对象
        return format_html(
            '<a href="{}">编辑</a>',
            # 反解 url地址
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    # 指示表头的展示文案
    operator.short_description = '操作'

    # 自定义静态资源
    # class Media:
    #     css = {
    #               'all': '',
    #           },
    #     js = ('',)


# 查看日志信息
from django.contrib.admin.models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag',
                    'user', 'change_message']
