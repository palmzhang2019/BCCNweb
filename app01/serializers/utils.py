from app01 import models
from rest_framework import serializers
import datetime


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.subjectList
        fields = ['id', 'name', "main_image"]


class SubjectDetailSerializer(serializers.ModelSerializer):
    article = serializers.SerializerMethodField()

    class Meta:
        model = models.subjectList
        fields = ["id", "name", "main_image", "brief", "article"]

    def get_article(self, obj):
        queryset = obj.article.all()
        return [{'id': row.id,
                 'name': row.name,
                 "post_datetime": row.post_datetime.strftime('%Y-%m-%d %H:%I:%S'),
                 "author": row.author,
                 "content": models.InstituteDetail.objects.filter(institute_id=row.id).first().content,
                 }
                for row in queryset]

