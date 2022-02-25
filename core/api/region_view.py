from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from core.models import Country, City, State
from core.permissions import DenyAny
from core.serializers import CountrySerializer, CitySerializer
from core.serializers.region_serializer import StateSerializer


class CountryViewSet(ModelViewSet):
    __basic_fields = ('name', 'cities__name')
    model = Country
    queryset = model.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def get_permissions(self):
        if self.action in ['create', 'bulk_create', 'update', 'partial_update',
                           'bulk_update', 'delete']:
            self.permission_classes = [DenyAny]
        return super().get_permissions()


class StateViewSet(ModelViewSet):
    __basic_fields = ('name', 'country__name')
    model = State
    queryset = model.objects.all()
    serializer_class = StateSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [DenyAny]
        return super().get_permissions()


class CityViewSet(ModelViewSet):
    __basic_fields = ('name', 'country__name', 'state__name')
    model = City
    queryset = model.objects.all()
    serializer_class = CitySerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [DenyAny]
        return super().get_permissions()

    def get_queryset(self):
        return super().get_queryset().select_related('country', 'state')
