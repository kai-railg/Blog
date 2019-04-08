__data__ = '2019-04-02 21:02'
__author__ = 'Kai'

from django.core.files.storage import Storage

from Blog import settings

from fdfs_client.client import Fdfs_client


class FDFSStorage(Storage):
    def __init__(self):
        self.conf = settings.FDFS_CLIENT_CONF
        self.url = settings.FDFS_NGINX_URL

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):

        client = Fdfs_client(self.conf)

        res = client.upload_appender_by_buffer(content.read())

        if res.get('Status') != 'Upload successed.':
            raise Exception('图片上传到 fastfds 存储系统时失败')

        filename = res.get('Remote file_id')

        return filename

    def exists(self, name):
        return False

    def url(self, name):
        return self.url + name
