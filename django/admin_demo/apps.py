from django.apps import AppConfig
from logger_demo import get_app_log_handler
from django.conf import settings


class AdminDemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_demo'
    logger = get_app_log_handler(name)

    @classmethod
    def ready(cls):
        cls.logger = get_app_log_handler(cls.name, **settings.APP_DEMO_LOGGER_CONFIG)
        # 在应用程序启动时执行的代码
        print(f"{cls.name} ready success")


def get_logger():
    return AdminDemoConfig.logger
