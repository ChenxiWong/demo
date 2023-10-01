from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 配置文件内容
from django.conf import settings
from .apps import get_logger

logger = get_logger()


def hello(request):
    logger.info("hello request")
    return HttpResponse("Hello, World!")
