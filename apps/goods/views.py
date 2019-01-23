import json
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Goods
from .serializes import GoodsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class GoodsListView(APIView):
    def get(self,request):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods,many=True)
        return Response(goods_serializer.data)