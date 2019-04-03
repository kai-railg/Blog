from django.shortcuts import render, reverse, redirect
from django.db import transaction
# Create your views here.
from .auth import PersonPermission

from pure_pagination import Paginator, PageNotAnInteger
from rest_framework.views import APIView

from user.models import Article, Tags, ArticleDetail


class IndexView(APIView):
    def get(self, request):
        article = Article.objects.all()
        # tag = request.GET.get('tag')
        # if tag:
        #     article = article.filter(tag=tag)
        # request.user.is_authenticated
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(article, 8)

        page_article = p.page(page)

        return render(request, 'index.html', {
            'article_list': page_article,
        })


class WriteView(APIView):
    permission_classes = [PersonPermission]

    def get(self, request):
        tags = Tags.objects.all()
        return render(request, 'add_article.html', {
            'tags': tags,
        })

    @transaction.atomic
    def post(self, request):
        id = request.POST.get('id')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        tag = request.POST.get('tag')
        content = request.POST.get('content')
        sid = transaction.savepoint()
        try:
            if not id:
                detail = ArticleDetail.objects.create(content=content)
                Article.objects.create(title=title, desc=desc, detail=detail, tag_id=tag)
            else:
                article = Article.objects.get(id=id)
                detail = article.detail.update(content=content)
                article.update(title=title, desc=desc, detail=detail, tag_id=tag)
        except Exception:
            transaction.savepoint_rollback(sid)
        return redirect('/')


class TagView(APIView):
    def get(self, request, tag):
        # if request.GET.get('filter'):
        #     return redirect('/')
        article = Article.objects.filter(tag=tag)
        # filter_id = request.GET.get('filter')
        # if filter_id:
        #     article = article.filter()
        # print(article[0].article.title)
        # tag_filter = Filter.objects.filter(tag=tag)[:4]
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(article, 8)

        page_article = p.page(page)

        return render(request, 'tag_page.html', {
            'article_list': page_article,
            # 'tag_filter': tag_filter,
        })


# from bs4 import BeautifulSoup

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
        return render(request, 'add_article.html', {
            'tags': tags,
            'article': article,
        })

    # @transaction.atomic
    # def post(self, request):
    #     title = request.POST.get('title')
    #     desc = request.POST.get('desc')
    #     tag = request.POST.get('tag')
    #     content = request.POST.get('content')
    #     sid = transaction.savepoint()
    #     try:
    #         detail = ArticleDetail.objects.create(content=content)
    #         article = Article.objects.create(title=title, desc=desc, detail=detail, tag_id=tag)
    #         # article.tag = tag
    #         # article.save()
    #     except Exception:
    #         transaction.savepoint_rollback(sid)
    #         return
    #     return redirect('/')

class DelArticleView(APIView):
    permission_classes = [PersonPermission]

    def get(self, request, article_id):
        Article.objects.filter(id=article_id).delete()
        return redirect('/')
