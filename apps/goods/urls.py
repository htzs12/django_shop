from django.urls import path,re_path
from . import views, views_demo



app_name = 'goods'

urlpatterns = [
    path('', views_demo.GoodsView.as_view(),name='goods'),
    # path('demo/', views.GoodsList1View.as_view(),name='goods1'),
]