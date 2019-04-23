
from django.conf import settings
from django.core.mail import send_mail

# 导入Celery类的对象
from celery import Celery


import os
import django

# 这两行代码需要初始化Django所依赖的环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ArchRL.settings")
django.setup()
app = Celery('celery_tasks.tasks', broker='redis://ip:6379/1')

# 定义任务
@app.task
def send_register_active_email(to_email, username, token):
    subject = '博客系统 欢迎您'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s, 欢迎您注册博客系统</h1><br/><a href="http://127.0.0.1:8000/active/%s">http://47.94.144.96:8888/user/active/%s</a>' % (
        username, token, token)

    send_mail(subject, message, sender, receiver, html_message=html_message)


