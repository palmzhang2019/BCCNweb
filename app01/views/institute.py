from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from app01 import models
from rest_framework.response import Response
from app01.serializers.institute import InstituteSerializer, InstituteDetailSerializer, InstituteRecSerializer
from app01.auth.auth import Auth

class InstituteView(ViewSetMixin, APIView):
    # authentication_classes = [Auth,]
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

    def create(self, request, *args, **kwargs):

        ret = {'code': 1000, 'data': None}
        data = request.data
        # 验证身份
        token = data['token']
        TokenObj = models.UserAuthToken.objects.filter(token=token)
        if not TokenObj:
            ret['code'] = '1004'
            ret['error'] = '身份验证失败'
            return Response(ret)
        userObj = models.Account.objects.get(pk=data['user_id'])
        tagObjlist = models.Tag.objects.filter(id__in=data['tag'])

        try:
            institute = models.Institute.objects.create(
                name=data['name'],
                author=userObj,
                main_image=data['main_image'],
            )
            institute.tag.add(*tagObjlist)
            models.InstituteDetail.objects.create(institute=institute, content=data['content'])
            ret['data'] = '添加成功'
        except Exception as e:
            ret['error'] = e
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