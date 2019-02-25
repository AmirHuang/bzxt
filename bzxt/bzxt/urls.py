"""bzxt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from bzxt.settings import MEDIA_ROOT
from users.views import UserViewset

router = DefaultRouter()

# 配置user
router.register(r'users', UserViewset, base_name='users')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),

    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf 文档 title自定义
    path('docs', include_docs_urls(title='Amir')),

    # drf 入口
    path('api-auth/', include('rest_framework.urls')),

    re_path(r'^', include(router.urls)),

    # jwt的认证接口
    re_path(r'^login/', obtain_jwt_token),
    re_path(r'^api-token-auth/', obtain_jwt_token),
]
