import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Goods, GoodsCategory
from .serializes import GoodsSerializer, GoodsCategorySerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


class GoodsListView(APIView):
    def get(self, request):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    # def post(self,request):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)


# class GoodsList1View(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)


# class GoodsList1View(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


class CategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list  商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
