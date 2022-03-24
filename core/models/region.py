from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    iso3 = models.CharField(max_length=5)
    iso2 = models.CharField(max_length=5)
    numeric_code = models.CharField(max_length=5)
    phone_code = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    currency_name = models.CharField(max_length=255)
    currency_symbol = models.CharField(max_length=255)
    tld = models.CharField(max_length=255)
    native = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255)
    subregion = models.CharField(max_length=255)
    timezones = models.JSONField(default=list)
    translations = models.JSONField(default=dict)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    emoji = models.CharField(max_length=191)
    emojiU = models.CharField(max_length=191)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)
    country_code = models.CharField(max_length=5)
    country_name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=255)
    type = models.CharField(max_length=255, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, related_name='cities', on_delete=models.CASCADE, null=True)
    state_code = models.CharField(max_length=255)
    state_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE, null=True)
    country_code = models.CharField(max_length=5)
    country_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wikiDataId = models.CharField(max_length=255)
