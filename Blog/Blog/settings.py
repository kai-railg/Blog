import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

SECRET_KEY = 'ip6x(^1)^dw7se@od8l4)xd8pfufpu=7rf164tr0f^##$r_+4a'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'crispy_forms',
    'pure_pagination',
    'rest_framework',
    'user',
]

# AUTHENTICATION_BACKENDS = (  # 元组方法，进行账号密码验证
#  'user.views.CustomBackend',  # 绑定自定义的验证账号密码 类
# )

AUTH_USER_MODEL = 'user.User'  # 配置继承 AbstractUser 的类

MIDDLEWARE = [
    # 'user.auth.MyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'Blog.urls'
WSGI_APPLICATION = 'Blog.wsgi.application'

# 邮箱配置
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = False  # 安全链接
# EMAIL_HOST = 'smtp.qq.com'  # qq就代表qq邮箱
# EMAIL_PORT = 25  # 端口号默认25
# EMAIL_HOST_USER = '1010547513@qq.com'  # 发件人的邮箱
# EMAIL_HOST_PASSWORD = 'ftkttstribqbbeic'  # 授权码
# EMAIL_FROM = 'Blog<1010547513@qq.com>'  # 发送邮件的邮箱 


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'HOST': '47.94.144.96',
        'USER': 'root',
        'PASSWORD': 'kai134680',
        'PORT': 3306,
    }
}

# 缓存
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://47.94.144.96:6379/5',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# session 存储引擎
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'  # 中国编码

TIME_ZONE = 'Asia/Shanghai'  # 上海时间

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# MEDIA_URL = '/media/'
#
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

REST_FRAMEWORK = {
    # 表示全局 开启频率组件
    # 'DEFAULT_THROTTLE_CLASSES':['app01.MyAuth.MyThrottling'],
    'DEFAULT_THROTTLE_RATES': {
        'person': '5/s'
    }
}

# 设置Django的文件存储类
DEFAULT_FILE_STORAGE = 'utils.fdfs.storage.FDFSStorage'

# 指定fdfs客户端配置文件的路径
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fdfs/client.conf')

# 指定fdfs系统机器上nginx的ip和port
FDFS_NGINX_URL = 'http://47.94.144.96:80/'
