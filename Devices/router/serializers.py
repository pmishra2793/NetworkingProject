from dataclasses import fields
from rest_framework import serializers
from router.models import RouterDetails


class RouterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouterDetails
        fields = '__all__'