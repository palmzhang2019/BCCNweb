from app01 import models
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = ["id", 'username', 'uid', 'openid', 'weights', 'balance']
