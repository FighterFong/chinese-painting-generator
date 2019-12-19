"""
WSGI config for artwork_creation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/

- python manage.py runserver：这是一款适合开发阶段使用的服务器，不适合运行在真实的生产环境中，在生产环境中使用WSGI

- WSGI：Web服务器网关接口，英文为Python Web Server Gateway Interface，缩写为WSGI，是Python应用程序或框架和Web服务器之间的一种接口，被广泛接受

- WSGI没有官方的实现, 因为WSGI更像一个协议，只要遵照这些协议,WSGI应用(Application)都可以在任何服务器(Server)上运行

- 命令django-admin startproject会生成一个简单的wsgi.py文件，确定了application、settings对象
application对象：在Python模块中使用application对象与应用服务器交互
settings模块：Django需要导入settings模块，这里是应用定义的地方

- 此处的服务器是一个软件，可以监听网卡端口、遵从网络层传输协议，收发http协议级别的数据
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artwork_creation.settings')

application = get_wsgi_application()
