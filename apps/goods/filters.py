# __author__ : htzs
# __time__   : 19-5-18 上午9:42


import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤
    """
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']