from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        # 声明抽象类
        abstract = True


class User(AbstractUser):
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Article(BaseModel):
    title = models.CharField(max_length=64, verbose_name='标题')
    desc = models.CharField(max_length=128, null=True, blank=True, verbose_name='简介')
    image = models.ImageField(upload_to='image', verbose_name='简介图片', default='', null=True)

    detail = models.OneToOneField(to='ArticleDetail', default='', null=False, verbose_name='文章详情')
    tag = models.ForeignKey(to='Tags', default='', verbose_name='所属标签')
    tag_filter = models.ForeignKey(to='Filter', default='', verbose_name='所属小标签', null=True, blank=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class ArticleDetail(BaseModel):
    content = models.TextField(verbose_name='正文')

    image = models.ImageField(upload_to='image', verbose_name='内容图片', default='', null=True)

    class Meta:
        verbose_name = '文章详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title


class Tags(models.Model):
    CHOICES = (
        ('1', 'Linux'),
        ('2', 'Python'),
        ('3', '数据库'),
        ('4', '数据结构'),
    )
    name = models.CharField(choices=CHOICES, max_length=32, verbose_name='标签名字')

    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Filter(models.Model):
    name = models.CharField(max_length=32, verbose_name='分类名字')
    tag = models.ForeignKey(to='Tags', default='', verbose_name='所属标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
