from rest_framework import serializers

from core.serializers.base_serializer import BaseSerializer


class FeeSerializer(BaseSerializer):
    tax = serializers.IntegerField(required=False)
    fee = serializers.IntegerField(required=False)
    currency = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    type = serializers.CharField(required=False, allow_null=True, allow_blank=True)


class KnownFeesSerializer(BaseSerializer):
    min_amount = serializers.FloatField(required=False, allow_null=True)
    max_amount = serializers.FloatField(required=False, allow_null=True)
    amount = serializers.FloatField(required=False, allow_null=True)
    currency = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    type = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    is_always_payable = serializers.IntegerField(required=False, allow_null=True)
    is_tax_included = serializers.IntegerField(required=False, allow_null=True)


class FeeBreakdownSerializer(BaseSerializer):
    known_fees = KnownFeesSerializer(required=False, many=True)


class PricingSerializer(BaseSerializer):
    price = serializers.FloatField(required=False)
    base_price = serializers.FloatField(required=False)
    drive_away_price_before = serializers.FloatField(required=False, allow_null=True)
    drive_away_price_is_approx = serializers.BooleanField(required=False)
    base_deposit = serializers.FloatField(required=False)
    drive_away_price = serializers.FloatField(required=False)
    base_currency = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    currency = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    quote_allowed = serializers.IntegerField(required=False)
    discount = serializers.FloatField(required=False)
    deposit = serializers.FloatField(required=False)
    fee_breakdown = FeeBreakdownSerializer(required=False)
