from rest_framework import serializers

from core.serializers.base_serializer import BaseSerializer
from core.serializers.filter_searializer import FilterSerializer
from core.serializers.pricing_serializer import PricingSerializer, FeeSerializer
from core.serializers.supplier_serializer import SupplierSerializer
from core.serializers.vehicle_serializer import VehicleSerializer


class SearchSortSerializer(BaseSerializer):
    name = serializers.CharField(required=False)
    identifier = serializers.CharField(required=False)
    title_tag = serializers.CharField(required=False)


class SearchResultSerializer(BaseSerializer):
    vehicle_info = VehicleSerializer(required=False)
    supplier_info = SupplierSerializer(required=False)
    pricing_info = PricingSerializer(required=False)
    fee_breakdown = FeeSerializer(required=False)
    fee_info = PricingSerializer(required=False)


class SearchSerializer(BaseSerializer):
    title = serializers.CharField(allow_null=True, allow_blank=True)
    type = serializers.CharField(allow_null=True, allow_blank=True)
    count = serializers.IntegerField(allow_null=True)
    is_genius_location = serializers.BooleanField()
    search_key = serializers.CharField(allow_null=True, allow_blank=True)
    filter = FilterSerializer(many=True)
    sort = SearchSortSerializer(many=True)
    search_results = SearchResultSerializer(many=True)
