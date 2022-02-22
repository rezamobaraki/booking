from rest_framework import serializers

from core.serializers.base_serializer import BaseSerializer


class LayoutSerializer(BaseSerializer):
    layout_type = serializers.CharField(required=False)
    is_collapsable = serializers.CharField(required=False)
    collapsed_count = serializers.IntegerField(required=False)
    is_collapsed = serializers.CharField(required=False)


class FilterCategories(BaseSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False, allow_null=True, allow_blank=True)


class FilterSerializer(BaseSerializer):
    id = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    layout = LayoutSerializer(required=False)
    categories = FilterCategories(many=True, required=False)
