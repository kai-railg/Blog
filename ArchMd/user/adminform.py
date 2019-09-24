__data__ = '2019-04-21 16:11'
__author__ = 'Kai'
from django import forms

from .models import Category, Tag, Article

from dal import autocomplete
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from ckeditor.widgets import CKEditorWidget   # 不支持图片上传


class ArticleAdminForm(forms.ModelForm):
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='category-autocomplete'),
    #     label='分类',
    # )
    # tag = forms.ModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
    #     label='标签',
    # )
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='正文',required=True)
    class Meta:
        model = Article
        fields = '__all__'
