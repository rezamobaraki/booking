from rest_framework import serializers

from core.models import Country, City, State


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id', 'name', 'iso3', 'iso2', 'numeric_code', 'phone_code', 'capital',
            'currency', 'currency_name', 'currency_symbol', 'tld', 'native',
            'region', 'subregion', 'timezones', 'translations',
            'latitude', 'longitude', 'emoji', 'emojiU',
        )
        read_only_fields = ("id",)


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            "id", "name", "country", "country_code", "country_name",
            "state_code", "type", "latitude", "longitude",
        )
        read_only_fields = ("id", "country")


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    state = StateSerializer()

    class Meta:
        model = City
        fields = (
            "id", "name", "state", "state_code", "state_name", "country", "country_code",
            "country_name", "latitude", "longitude", "wikiDataId",
        )
        read_only_fields = ("id", "state", "country")
