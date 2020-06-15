from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from app01 import models
from rest_framework.response import Response
from app01.serializers.institute import InstituteSerializer, InstituteDetailSerializer, InstituteRecSerializer


class InstituteView(ViewSetMixin, APIView):
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
            if rank_method == "hot":
                queryset = models.Institute.objects.all().order_by("-view_num")[:6]
            else:
                queryset = models.Institute.objects.all()
            ser = InstituteSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取学院帖子失败'


        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        """
        课程详细接口
        """
        ret = {'code': 1000, 'data': None}
        try:
            # 课程ID=2
            pk = kwargs.get('pk')
            # 课程详细对象
            obj = models.InstituteDetail.objects.filter(institute_id=pk).first()
            ser = InstituteDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程详细失败'
        return Response(ret)

class InstituteRecView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = models.InstituteRec.objects.all().order_by("-weights")
            ser = InstituteRecSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取学院帖子失败'


        return Response(ret)