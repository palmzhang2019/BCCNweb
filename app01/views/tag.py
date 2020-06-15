from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from app01 import models
from rest_framework.response import Response
from app01.serializers.tag import TagSerializer


class TagView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            queryset = models.Tag.objects.all()
            ser = TagSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取标签失败'

        return Response(ret)