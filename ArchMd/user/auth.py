__data__ = '2019-04-02 17:28'
__author__ = 'Kai'
import uuid
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
from django.core.cache import cache

from rest_framework.permissions import BasePermission
from rest_framework.throttling import SimpleRateThrottle


class PersonPermission(BasePermission):
    massage = '非访问内容'

    def has_permission(self, request, view):
        if request.user.username != 'wangkai':
            return False
        return True


class PersonThrottling(SimpleRateThrottle):
    scope = 'person'

    def get_cache_key(self, request, view):
        return request.META.get('REMOTE_ADDR')


class CommonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        addr = request.META.get('REMOTE_ADDR')
        if len(cache.get(addr, [])) >= 3:
            raise PermissionDenied('Forbidden user agent')

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Headers'] = '*'
            response['Access-Control-Allow-Methods'] = '*'
        return response


# 创建token
class UserIdMiddle:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        uid = self.token(request)
        request.uid = uid
        response = self.get_response(request)
        response.set_cookie('article', uid, httponly=True)
        return response

    def token(self, request):
        token = request.COOKIES.get('article')
        if not token:
            token = uuid.uuid4().hex
        return token
