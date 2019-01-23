from django.urls import path,re_path
from . import views


app_name = 'goods'

urlpatterns = [
    path('', views.GoodsListView.as_view(),name='goods'),
]