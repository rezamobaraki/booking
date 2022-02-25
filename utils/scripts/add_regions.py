import json

from django.conf import settings

from core.models import City, State, Country


def seed_countries():
    with open(f"{settings.BASE_DIR}/utils/data/json/country-state-city/countries.json", encoding="utf-8") as data_file:
        json_data = json.loads(data_file.read())
        for obj in json_data:
            Country.objects.create(**obj)


def seed_states():
    with open(f"{settings.BASE_DIR}/utils/data/json/country-state-city/states.json", encoding="utf-8") as data_file:
        json_data = json.loads(data_file.read())
        for obj in json_data:
            State.objects.create(**obj)


def seed_cities():
    with open(f"{settings.BASE_DIR}/utils/data/json/country-state-city/cities.json", encoding="utf-8") as data_file:
        json_data = json.loads(data_file.read())
        for obj in json_data:
            City.objects.create(**obj)
