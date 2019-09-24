from django.db import models

from django.contrib.auth.models import User

class BaseModel(models.Model):
    user = models.ForeignKey(User, verbose_name='作者', null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    status = models.BooleanField(default=1, verbose_name='正常')

    class Meta:
        abstract = True


class Category(BaseModel):
    LINUX = 1
    PYTHON = 2
    DATABASE = 3
    STRUCTURE = 4
    CHOICES = (
        (LINUX, 'Linux'),
        (PYTHON, 'Python'),
        (DATABASE, '数据库'),
        (STRUCTURE, '数据结构'),
    )
    name = models.PositiveIntegerField(choices=CHOICES, verbose_name='分类')

    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(BaseModel):
    name = models.CharField(max_length=32, verbose_name='标签名字')
    category = models.ForeignKey(Category, verbose_name='分类', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Article(BaseModel):
    STATUS_DELETE = 0
    STATUS_NORMAL = 1
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, verbose_name='状态', default=1)
    category = models.ForeignKey(Category, verbose_name='分类', null=True)
    tag = models.ForeignKey(Tag, verbose_name='标签', null=True)
    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, verbose_name='摘要')
    content = models.TextField(help_text='正文必须为MakeDown格式', verbose_name='正文')
    # 访问量
    pv = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='image', verbose_name='简介图片', blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    #
    # from django.utils.functional import cached_property
    # 把返回的函数绑定到实例上，但是因为我们的tag 不是多对多关系，所以这里就不用了
    # @cached_property
    # def tags(self):
    #     return ','.join(self.tag.values_list('name', flat=True))