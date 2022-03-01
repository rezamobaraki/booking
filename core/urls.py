from rest_framework.routers import DefaultRouter

from core.api import CountryViewSet
from core.api.booking_view import VehicleViewSet
from core.api.region_view import CityViewSet, StateViewSet

app_name = 'core'
router = DefaultRouter()

router.register(r'rental', VehicleViewSet, basename='vehicles')
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'states', StateViewSet, basename='states')
router.register(r'cities', CityViewSet, basename='cities')

urlpatterns = router.urls
