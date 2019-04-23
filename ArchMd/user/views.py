from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.db import transaction
from django.core.cache import cache

from .models import Article, Category, Tag
from .auth import PersonPermission

from rest_framework.views import APIView
from django_redis import get_redis_connection
from silk.profiling.profiler import silk_profile


class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 1
    queryset = Article.objects.all(). \
        select_related('category'). \
        select_related('tag'). \
        defer('content')
    context_object_name = 'article_list'
    ordering = '-created_time'

    @silk_profile(name='IndexView.get_queryset')
    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category_id=int(category))
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(category_id=int(tag))
        return queryset

    def get_context_data(self, **kwargs):
        content = cache.get('index_page_date')
        if not content:
            content = super(IndexView, self).get_context_data()
            tags = Tag.objects.all()[:10]
            categories = Category.objects.all()
            content.update({
                'tags': tags,
                'categories': categories,
            })
            content['view'] = None
            cache.set('index_page_date', content, 3600)
        return content


class DetailArticle(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'
    conn = get_redis_connection()

    def get(self, request, *args, **kwargs):
        id = str(self.kwargs.get(self.pk_url_kwarg))
        detail = cache.get(f'detail{id}')
        if detail:
            self.object = detail
        else:
            self.object = self.get_object()
            cache.set(f'detail{id}', self.object, 3600)
        try:
            pv = int(self.conn.hget('article', id))
        except TypeError:
            pv = 1
        self.object.pv = pv
        token = request.COOKIES.get('article')
        if not self.conn.get(token + id):
            self.conn.hset('article', id, pv + 1)
            self.conn.setex(token + id, 3600 * 24, id)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class WriteView(APIView):
    permission_classes = [PersonPermission]

    def get(self, request):
        id = request.GET.get('article_id')
        article = None
        if id:
            article = Article.objects.get(id=id)
        tags = Tag.objects.all()
        categories = Category.objects.all()
        return render(request, 'add_article.html', {
            'article': article,
            'tags': tags,
            'categories': categories,
        })

    @transaction.atomic
    def post(self, request):
        id = request.POST.get('id')
        if not id:
            try:
                id = Article.objects.last().id + 1
            except AttributeError:
                id = 1
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        tag = request.POST.get('tag')
        category = request.POST.get('category', None)
        content = request.POST.get('content')
        sid = transaction.savepoint()
        try:
            default = {'title': title, 'desc': desc, 'tag_id': tag,
                       'category_id': category, 'content': content}
            Article.objects.update_or_create(id=id, defaults=default)
        except Exception:
            transaction.savepoint_rollback(sid)
        return redirect('/')


class DelArticleView(APIView):
    permission_classes = [PersonPermission]

    def get(self, request, article_id):
        Article.objects.filter(id=article_id).delete()
        return redirect('/')


# handler404 = Handler404.as_view()
# handler500 = Handler50x.as_view()

class Handler404(TemplateView):
    template_name = '404.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)
