__data__ = '2019-04-20 20:35'
__author__ = 'Kai'

import django
import os
from ArchMd import settings
from celery import Celery
from django.template import loader

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ArchMd.settings")
# django.setup()



app = Celery('test', broker='redis://47.94.144.96:6379/1', backend='redis://47.94.144.96:6379/2')



@app.task
def generate_static_index_html():
    from user.views import IndexView
    content = IndexView().get_context_data()
    # 1. 加载模版
    temp = loader.get_template('static_index.html')
    # 2  渲染模版
    static_html = temp.render(content)
    # 3 创建静态首页文件
    save_path = os.path.join(settings.BASE_DIR, 'static/index .html')
    with open(save_path, 'w') as f:
        f.write(static_html)
