from rest_framework import serializers

from core.serializers.base_serializer import BaseSerializer


class SuitcasesSerializer(BaseSerializer):
    small = serializers.IntegerField()
    big = serializers.IntegerField()


class VehicleSerializer(BaseSerializer):
    v_id = serializers.IntegerField()
    v_name = serializers.CharField(allow_null=True, allow_blank=True)
    seats = serializers.IntegerField()
    doors = serializers.IntegerField()
    airbags = serializers.BooleanField()
    aircon = serializers.BooleanField()
    unlimited_mileage = serializers.BooleanField
    free_cancellation = serializers.IntegerField()
    suitcases = SuitcasesSerializer()
    image_url = serializers.URLField()
    image_thumbnail_url = serializers.URLField()
    group = serializers.CharField(allow_null=True, allow_blank=True)
    label = serializers.CharField(allow_null=True, allow_blank=True)
    fuel_policy = serializers.CharField(allow_null=True, allow_blank=True)
    special_offer_text = serializers.CharField(allow_null=True, allow_blank=True)
    fuel_policy_description = serializers.CharField(allow_null=True, allow_blank=True)
    fuel_type = serializers.CharField(allow_null=True, allow_blank=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
