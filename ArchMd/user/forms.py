__data__ = '2019-04-20 16:14'
__author__ = 'Kai'

from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['pv', 'image']
