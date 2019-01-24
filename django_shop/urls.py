"""django_shop URL Configuration

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
from django.contrib import admin
import xadmin
from django.urls import path,re_path,include
from django_shop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListView,CategoryViewset

router = DefaultRouter()
router.register(r'goods',GoodsListView,base_name='goods')
router.register(r'categorys',CategoryViewset,base_name='categorys')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('goods/', include('goods.urls')),
    path('docs/', include_docs_urls(title='haoge')),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),

    # 处理图片显示的url,使用django自带server，传入参数告诉它去哪里找，我们有配置好的路径MEDIA_ROOT
    re_path('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
]
