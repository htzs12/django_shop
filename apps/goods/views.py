import json
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Goods
from .serializes import GoodsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class GoodsListView(APIView):
    def get(self,request):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods,many=True)
        return Response(goods_serializer.data)

    # def post(self,request):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)


class GoodsList1View(mixins.ListModelMixin,generics.GenericAPIView):
    pass