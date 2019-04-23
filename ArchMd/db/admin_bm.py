__data__ = '2019-04-19 13:43'
__author__ = 'Kai'
from django.contrib import admin
from django.core.cache import cache

from utils.celery_task import generate_static_index_html







class BaseOwnerAdmin(admin.ModelAdmin):
    # exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
        # 重新生成静态页面
        generate_static_index_html.delay()
        cache.delete('index_page_date')

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        generate_static_index_html.delay()
        cache.delete('index_page_date')

    # 控制当前用户的数据显示，使用户数据展示不造成泄漏
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)
