from rest_framework import serializers

from core.serializers.base_serializer import BaseSerializer
from core.serializers.pricing_serializer import PricingSerializer, FeeSerializer
from core.serializers.supplier_serializer import SupplierSerializer
from core.serializers.vehicle_serializer import VehicleSerializer


class SearchResultSerializer(BaseSerializer):
    vehicle_info = VehicleSerializer(required=False)
    supplier_info = SupplierSerializer(required=False)
    fee_breakdown = FeeSerializer(required=False)
    fee_info = PricingSerializer(required=False)


class SearchSerializer(BaseSerializer):
    title = serializers.CharField(allow_null=True, allow_blank=True)
    type = serializers.CharField(allow_null=True, allow_blank=True)
    count = serializers.IntegerField(allow_null=True)
    search_key = serializers.CharField(allow_null=True, allow_blank=True)
    search_results = SearchResultSerializer(many=True)
