from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_article$', views.WriteView.as_view(), name='add_article'),
    url(r'^article/(?P<article_id>\d+).html', views.DetailArticle.as_view(), name='article'),
    url(r'^delete/(?P<article_id>\d+)', views.DelArticleView.as_view(), name='del_article'),
]

