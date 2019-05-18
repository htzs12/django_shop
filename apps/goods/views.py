import json
from .models import Goods, GoodsCategory
from .serializes import GoodsSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
# from django_filters import rest_framework as filters
from .filters import GoodsFilter
from rest_framework import filters


# class GoodsListView(APIView):
#     def get(self, request):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# class GoodListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     list  商品列表数据
#     """
#     # queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination
#
#     def get_queryset(self):
#         queryset = Goods.objects.all()
#         price_min = self.request.query_params.get('price_min', 0)
#         if price_min:
#             queryset = queryset.filter(shop_price__gt=int(price_min))
#         return queryset


class GoodListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list  商品列表数据
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # filter_fields = ('name', 'shop_price')
    # filter_class = GoodsFilter
    # search_fields = ('name',)
    #
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))
    #     return queryset


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list  商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
