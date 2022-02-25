from rest_framework.routers import DefaultRouter

from core.api import CountryViewSet, VehicleViewSet
from core.api.region_view import CityViewSet, StateViewSet

router = DefaultRouter()

router.register(r'vehicles', VehicleViewSet, basename='vehicles')
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'states', StateViewSet, basename='states')
router.register(r'cities', CityViewSet, basename='cities')
