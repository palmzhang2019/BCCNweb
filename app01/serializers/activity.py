from app01 import models
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()
    partner = serializers.SerializerMethodField()
    important_guests = serializers.SerializerMethodField()
    activity_status = serializers.CharField(source="get_activity_status_display")
    activity_type = serializers.CharField(source="get_activity_type_display")
    datetime_start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    datetime_end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = models.Activity
        fields = ['id', 'name', 'datetime_start', 'datetime_end', 'number_people', 'address', 'main_image', "view_number",
                  "tag", "collect_number", "partner", "important_guests", "activity_status", "activity_type"]

    def get_tag(self, obj):
        queryset = obj.tag.all()
        return [{'id': row.id, 'name': row.name} for row in queryset]

    def get_partner(self, obj):
        queryset = obj.partner.all()
        return [{'id': row.id, 'name': row.name} for row in queryset]

    def get_important_guests(self, obj):
        queryset = obj.important_guests.all()
        return [{'id': row.id, 'name': row.username} for row in queryset]


class ActivityDetailSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source="activity.name")
    datetime_start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True, source="activity.datetime_start")
    datetime_end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True, source="activity.datetime_end")
    main_image = serializers.ImageField(source="activity.main_image")

    tag = serializers.SerializerMethodField()
    partner = serializers.SerializerMethodField()
    important_guests = serializers.SerializerMethodField()
    activity_status = serializers.CharField(source="activity.get_activity_status_display")
    activity_type = serializers.CharField(source="activity.get_activity_type_display")

    number_people = serializers.IntegerField(source="activity.number_people")
    address = serializers.CharField(source="activity.address")
    view_number = serializers.IntegerField(source="activity.view_number")
    collect_number = serializers.IntegerField(source="activity.collect_number")
    orderpeople_num = serializers.IntegerField(source="activity.orderpeople_num")
    class Meta:
        model = models.ActivityDetail
        fields = '__all__'

    def get_tag(self, obj):
        queryset = obj.activity.tag.all()
        return [{'id': row.id, 'name': row.name} for row in queryset]

    def get_partner(self, obj):
        queryset = obj.activity.partner.all()
        return [{'id': row.id, 'name': row.name} for row in queryset]

    def get_important_guests(self, obj):
        queryset = obj.activity.important_guests.all()
        return [{'id': row.id, 'name': row.username} for row in queryset]