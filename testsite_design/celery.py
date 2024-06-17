
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 设置 Django 默认的配置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testsite_design.settings')

app = Celery('testsite_design')

# 从 Django 的 settings.py 中导入所有 Celery 配置
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现每个 Django app 中的 tasks.py 文件
app.autodiscover_tasks()
