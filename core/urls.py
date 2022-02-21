from rest_framework.routers import DefaultRouter

from core.views import VehicleViewSet

router = DefaultRouter()

router.register(r'vehicles', VehicleViewSet, basename='vehicles')
