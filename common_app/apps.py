from django.apps import AppConfig


class CommonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common_app'
    verbose_name = '测试数据'
