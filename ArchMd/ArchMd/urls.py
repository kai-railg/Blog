"""ArchMd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_view
from django.conf.urls.static import static

from utils.rss import LatestArticleFeed
from utils.sitemap import ArticleSitemap
from utils.admin_site import custom_site
from utils.autocomplete import TagAc, CategoryAC
from ArchMd import settings

import debug_toolbar

urlpatterns = [
    url(r'^super_admin/', admin.site.urls),
    url(r'^admin/', custom_site.urls),

    url(r'^search/', include('haystack.urls')),

    url(r'^ckeditor/',include('ckeditor_uploader.urls')),

    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^silk/', include('silk.urls', namespace='silk')),


    url(r'^rss|feed/', LatestArticleFeed(), name='rss'),
    url(r'sitemap\.xml', sitemap_view.sitemap, {'sitemaps': {'posts': ArticleSitemap}}),

    url(r'^category-autocomplete/$', CategoryAC.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAc.as_view(), name='tag-autocomplete'),

    url(r'^resume/$', TemplateView.as_view(template_name='resume.html'), name='resume'),
    url(r'^', include('user.urls', namespace='user')),
]

# 配置图片访问
static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)