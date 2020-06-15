from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from app01 import models
from rest_framework.response import Response
from app01.serializers.account import AccountSerializer


class AccountView(ViewSetMixin, APIView):
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
                queryset = models.Account.objects.filter(weights=3)[:5]
            elif rank_method == "silver":
                queryset = models.Account.objects.filter(weights=2)[:5]
            elif rank_method == "bronze":
                queryset = models.Account.objects.filter(weights=1)[:5]
            elif rank_method == "general":
                queryset = models.Account.objects.filter(weights=0)[:5]
            else:
                queryset = models.Account.objects.all()
            ser = AccountSerializer(instance=queryset, many=True)
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
            obj = models.Account.objects.filter(id=pk).first()
            ser = AccountSerializer(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程详细失败'
        return Response(ret)
