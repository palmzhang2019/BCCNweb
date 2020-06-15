from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from app01 import models
from rest_framework.response import Response
from app01.serializers.product import ProductSerializer, ProductDetailSerializer


class ProductView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        rank_method = request.query_params.dict().get("q")
        try:
            if rank_method == "gold":
                queryset = models.Products.objects.filter()
            elif rank_method == "silver":
                queryset = models.Products.objects.filter()
            elif rank_method == "bronze":
                queryset = models.Products.objects.filter()
            elif rank_method == "general":
                queryset = models.Products.objects.filter()
            else:
                queryset = models.Products.objects.all()
            ser = ProductSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取会员帖子失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            # 课程ID=2
            pk = kwargs.get('pk')
            # 课程详细对象
            obj = models.ProductsDetail.objects.filter(id=pk).first()
            ser = ProductDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程详细失败'
        return Response(ret)
