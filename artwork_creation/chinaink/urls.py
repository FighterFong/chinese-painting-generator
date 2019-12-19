#encoding:utf-8
'''
    路由信息表
'''
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    #()获取数据，正则三大功能（匹配，提取，替换）
    path('index', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('add', views.add, name='add'),
    path('Captcha', views.Captcha, name='Captcha'),
    path('cal', views.cal, name='Calculate'),
    # path(r'^upload1', views.upload1),
    # path(r'^shangchuan', views.shangchuan),
    # path(r'^multiple', views.multiple),
    # path(r'^ajax',views.ajax),
    # path(r'^ajax_deal',views.ajax_deal),
    # path(r'^add', views.add),
]