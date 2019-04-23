__data__ = '2019-04-22 18:25'
__author__ = 'Kai'

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from user.models import Article

from django_redis import get_redis_connection


# 保存数据时同时设置缓存
@receiver(post_save, sender=Article)
def after_save(sender, instance=None, **kwargs):
    conn = get_redis_connection()
    try:
        conn.hset('detail', instance.id, instance)
    except TypeError:
        pass


# 删除数据时删除缓存
@receiver(post_delete, sender=Article)
def after_save(sender, instance=None, **kwargs):
    conn = get_redis_connection()
    try:
        conn.hdel('detail', instance.id)
    except TypeError:
        pass
