__data__ = '2019-04-21 14:50'
__author__ = 'Kai'

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from user.models import Article

class ArticleSitemap(Sitemap):
    changefrep = 'always'
    priority = 1.0
    protocol = 'http'

    # 返回正常状态的文章
    def items(self):
        return Article.objects.filter(status=Article.STATUS_NORMAL)
    # 返回文章的创建日期
    def lastmod(self, obj):
        return obj.created_time
    # 返回文章的url
    def location(self, obj):
        return reverse('user:article', args=[obj.pk])