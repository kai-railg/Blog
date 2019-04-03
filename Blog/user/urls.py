"""Blog URL Configuration

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
from django.conf.urls import url
from . import views

urlpatterns = [
    # 首页
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 添加文章
    url(r'^add_article$', views.WriteView.as_view(), name='add_article'),
    # 分类下的文章
    url(r'^tag/(?P<tag>\d+)', views.TagView.as_view(), name='tag'),
    # 文章详情
    url(r'^article/(?P<article_id>\d+)', views.ArticleView.as_view(), name='article'),
    # 编辑文章
    url(r'^edit/(?P<article_id>\d+)', views.EditArticleView.as_view(), name='edit_article'),
    # 删除文章
    url(r'^delete/(?P<article_id>\d+)', views.DelArticleView.as_view(), name='del_article'),
]

