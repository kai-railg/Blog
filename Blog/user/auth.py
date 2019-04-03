__data__ = '2019-04-02 17:28'
__author__ = 'Kai'

from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from rest_framework.throttling import SimpleRateThrottle


class PersonPermission(BasePermission):
    massage = '非访问内容'

    def has_permission(self, request, view):
        # 后台管理只绑定一个管理员id
        if request.user.username != 'wangkai':
            return False
        return True


class PersonThrottling(SimpleRateThrottle):
    scope = 'person'

    def get_cache_key(self, request, view):
        return request.META.get('REMOTE_ADDR')


from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # 处理了简单请求
        response['Access-Control-Allow-Origin'] = '*'
        # 处理非简单请求
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Headers'] = '*'
            # response['Access-Control-Allow-Methods']='PUT,PATCH'
            response['Access-Control-Allow-Methods'] = '*'

        return response
