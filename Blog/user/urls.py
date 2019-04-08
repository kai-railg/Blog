from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_article$', views.WriteView.as_view(), name='add_article'),
    url(r'^tag/(?P<tag>\d+)', views.TagView.as_view(), name='tag'),
    url(r'^article/(?P<article_id>\d+)', views.ArticleView.as_view(), name='article'),
    url(r'^edit/(?P<article_id>\d+)', views.EditArticleView.as_view(), name='edit_article'),
    url(r'^delete/(?P<article_id>\d+)', views.DelArticleView.as_view(), name='del_article'),
]

