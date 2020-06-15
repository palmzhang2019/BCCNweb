from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from app01 import models
from rest_framework.response import Response
from app01.serializers.activity import ActivitySerializer, ActivityDetailSerializer


class ActivityView(ViewSetMixin, APIView):
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
            queryset = models.Activity.objects.all()
            ser = ActivitySerializer(instance=queryset, many=True)
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
            obj = models.ActivityDetail.objects.filter(activity_id=pk).first()
            ser = ActivityDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程详细失败'
        return Response(ret)

    def create(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        activity_id = int(request.data.get("activity_id"))
        user_id = int(request.data.get("user_id"))

        activityObj = models.Activity.objects.filter(pk=activity_id).first()
        if not activityObj:
            ret['code'] = 4000
            ret['error'] = "没有该活动"
            return Response(ret)
        accountObj = models.Account.objects.filter(pk=user_id).first()
        if not accountObj:
            ret['code'] = 4002
            ret['error'] = "没有该用户"
            return Response(ret)
        account_list = activityObj.account_set.all()
        if accountObj in account_list:
            ret['code'] = 5000
            ret['error'] = '已经添加过了，请勿再添加'
        else:
            activityObj.account_set.add(accountObj)
            ret['msg'] = '已报名'
        return Response(ret)