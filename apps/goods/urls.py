from django.urls import path, re_path
from . import views, views_demo

app_name = 'goods'


good_list = views.GoodListViewset.as_view({
    'get': 'list',
    # 'post': 'create'
})

urlpatterns = [
    path('', views.GoodsListView.as_view(), name='goods'),
    path('list/', good_list, name='goods_list'),
]
