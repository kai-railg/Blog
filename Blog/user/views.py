from django.shortcuts import render, reverse, redirect
from django.db import transaction

from user.models import Article, Tags, ArticleDetail, Filter
from .auth import PersonPermission

from pure_pagination import Paginator, PageNotAnInteger
from rest_framework.views import APIView


class IndexView(APIView):
    def get(self, request):
        article = Article.objects.all().order_by('-position').order_by('-create_time')
        _filter = Filter.objects.all()

        _tag = request.GET.get('filter')
        if _tag:
            article = article.filter(tag_filter=_tag)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(article, 8)

        page_article = p.page(page)

        content = {
            'article_list': page_article,
            'tag_filter': _filter,
        }
        return render(request, 'index.html', content)

class WriteView(APIView):
    permission_classes = [PersonPermission]

    def get(self, request):
        tags = Tags.objects.all()
        tag_filter = Filter.objects.all()
        return render(request, 'add_article.html', {
            'tags': tags,
            'tag_filter': tag_filter,
        })

    @transaction.atomic
    def post(self, request):
        id = request.POST.get('id')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        tag = request.POST.get('tag', None)
        _filter = request.POST.get('filter', None)
        _position = request.POST.get('position', 0)
        content = request.POST.get('content')
        sid = transaction.savepoint()
        try:
            if not id:
                detail = ArticleDetail.objects.create(content=content)
                Article.objects.create(title=title, desc=desc, detail=detail,
                                       tag_id=tag, tag_filter_id=_filter, position=_position)
            else:
                article = Article.objects.filter(id=id)
                detail = article[0].detail
                detail.content = content
                detail.save()
                article.update(title=title, desc=desc, detail=detail, tag_id=tag,
                               tag_filter_id=_filter, position=_position)
        except Exception as e:
            transaction.savepoint_rollback(sid)
            return
        return redirect('/')


class TagView(APIView):
    def get(self, request, tag):
        article = Article.objects.filter(tag=tag).order_by('-position').order_by('-create_time')
        _filter = Filter.objects.all()

        _tag = request.GET.get('filter')
        if _tag:
            article = article.filter(tag_filter=_tag)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(article, 8)

        page_article = p.page(page)

        return render(request, 'tag_page.html', {
            'article_list': page_article,
            'tag_filter': _filter,
        })


class ArticleView(APIView):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        return render(request, 'article_detail.html', {
            'article': article,
        })


class EditArticleView(APIView):
    permission_classes = [PersonPermission]

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        tags = Tags.objects.all()
        tag_filter = Filter.objects.all()
        return render(request, 'add_article.html', {
            'tags': tags,
            'article': article,
            'tag_filter': tag_filter,
        })


class DelArticleView(APIView):
    permission_classes = [PersonPermission]

    def get(self, request, article_id):
        Article.objects.filter(id=article_id).delete()
        return redirect('/')


from django.shortcuts import render_to_response
# 404对应处理view
def page_not_found(request):

    response = render_to_response("404.html", {
    })
    # 设置response的状态码
    response.status_code = 404
    return response
