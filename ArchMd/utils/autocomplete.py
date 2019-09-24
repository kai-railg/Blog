__data__ = '2019-04-21 15:20'
__author__ = 'Kai'

from dal import autocomplete
from user.models import Category, Tag


class CategoryAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Category.objects.none()
        queryset = Category.objects.filter(user=self.request.user)
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset


class TagAc(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()
        qs = Tag.objects.filter(user=self.request.user)
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs
