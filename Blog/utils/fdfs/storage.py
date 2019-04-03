__data__ = '2019-04-02 21:02'
__author__ = 'Kai'

# django 的文件存储系统
from django.core.files.storage import Storage

from Blog import settings

from fdfs_client.client import Fdfs_client


# 重写方法
class FDFSStorage(Storage):
    def __init__(self):
        self.conf = settings.FDFS_CLIENT_CONF
        self.url = settings.FDFS_NGINX_URL

    def _open(self, name, mode='rb'):
        # 打开文件时使用
        pass

    def _save(self, name, content):
        '''
        :param name:  上传文件的名字
        :param content:  文件对象
        :return:
        '''
        # 1 加载配置文件，创建 Fdfs_client 对象

        client = Fdfs_client(self.conf)

        # 2 上传文件到 fdfs 存储系统中, 文件内容从 contetn 中读取
        res = client.upload_appender_by_buffer(content.read())

        #  上传成功， 返回的格式 {
        #         #     'Group name'      : group_name,
        #         #     'Remote file_id'  : remote_file_id,
        #         #     'Status'          : 'Upload successed.',
        #         #     'Local file name' : '',
        #         #     'Uploaded size'   : upload_size,
        #         #     'Storage IP'      : storage_ip
        #         # }

        # 3 判断是否上传成功
        if res.get('Status') != 'Upload successed.':
            raise Exception('图片上传到 fastfds 存储系统时失败')

        # 4 上传成功，返回文件在fdfs 中的id， 比如 /group/M00/00/...
        filename = res.get('Remote file_id')

        # 5 返回id， 数据库中存的就是这个值
        return filename

    def exists(self, name):
        '''
        Django 判断文件名是否可用的方法
        :param name:
        :return: False ： 表示可用； True： 表示不可用
        '''
        return False

    def url(self, name):
        ''' 返回访问文件的url 路径'''
        return self.url + name
