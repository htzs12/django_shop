import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Goods


class GoodsView(View):
    def get(self, request):
        goods = Goods.objects.all()[:10]
        json_list = []

        # for good in goods:
        #     goods_dict = {}
        #     goods_dict['name'] = good.name
        #     goods_dict['category'] = good.category.name
        #     goods_dict['market_price'] = good.market_price
        #     json_list.append(goods_dict)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # return HttpResponse(json_list)

        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        return HttpResponse(json_data, content_type='application/json')
