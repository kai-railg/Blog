__data__ = '2019-04-21 14:39'
__author__ = 'Kai'

from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from user.models import Article


class ExtendRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement('content:html', item['content'])


class LatestArticleFeed(Feed):
    feed_type = ExtendRSSFeed
    title = 'Kai blog system'
    link = '/rss/'
    description = 'Kai blog system has update'

    def items(self):
        return Article.objects.filter(status=Article.STATUS_NORMAL)[:5]

    def item_title(self, item):
        return self.title

    def item_description(self, item):
        return self.description

    def item_link(self, item):
        return reverse('user:article', args=[item.pk])

    def item_extra_kwargs(self, item):
        return {'content': self.item_content(item)}

    def item_content(self, item):
        return item.content
