from app01 import models
from rest_framework import serializers


class InstituteSerializer(serializers.ModelSerializer):
    post_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    tag = serializers.SerializerMethodField()
    author = serializers.CharField()
    author_id = serializers.IntegerField()

    class Meta:
        model = models.Institute
        fields = ['id', 'name','author_id', 'post_datetime', 'author', 'thumb_up', 'view_num', 'reply_num', 'main_image', "tag"]

    def get_tag(self, obj):
        queryset = obj.tag.all()
        return [{'id': row.id, 'name': row.name} for row in queryset]



class InstituteDetailSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source="institute.name")
    author = serializers.CharField(source="institute.author")
    author_id = serializers.IntegerField(source="institute.author_id")
    main_image = serializers.ImageField(source="institute.main_image")

    class Meta:
        model = models.InstituteDetail
        fields = '__all__'

class InstituteRecSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="institute.name")
    post_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False,
                                              read_only=True, source="institute.post_datetime")
    author = serializers.CharField(source="institute.author")
    thumb_up = serializers.IntegerField(source="institute.thumb_up")
    view_num = serializers.IntegerField(source="institute.view_num")
    reply_num = serializers.IntegerField(source="institute.reply_num")
    main_image = serializers.ImageField(source="institute.main_image")

    class Meta:
        model = models.InstituteRec
        fields = ["id", "name", "post_datetime", "author", "thumb_up", "view_num", "reply_num", "main_image", "weights"]


