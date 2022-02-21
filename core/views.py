import json

import requests
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.serializers.search_serializer import SearchSerializer


class VehicleViewSet(ViewSet):
    serializer_class = SearchSerializer

    @action(detail=False, methods=["get"], permission_classes=[])
    def search_car(self, request, *args, **kwargs):
        url = "https://booking-com.p.rapidapi.com/v1/car-rental/search"

        querystring = {"drop_off_datetime": "2022-08-06 12:00:00", "sort_by": "recommended",
                       "pick_up_datetime": "2022-08-05 12:00:00", "pick_up_latitude": "55.7518540820001",
                       "from_country": "it", "locale": "en-gb", "drop_off_latitude": "55.7518540820001",
                       "drop_off_longitude": "37.620230899", "pick_up_longitude": "37.620230899", "currency": "AED"}

        headers = {
            'x-rapidapi-host': "booking-com.p.rapidapi.com",
            'x-rapidapi-key': "910e503bf3msh01b90ab3b1811d8p15372bjsn7670471df649"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        contex = json.loads(response.content)
        serialized_data = SearchSerializer(data=contex)
        if serialized_data.is_valid():
            return Response(serialized_data.data, status=status.HTTP_200_OK)
