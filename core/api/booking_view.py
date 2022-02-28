import json

import requests
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.models.booking import SearchBooking
from core.serializers.search_serializer import SearchSerializer


class VehicleViewSet(ViewSet):
    api_url = "https://booking-com.p.rapidapi.com/v1/car-rental/search"
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    @action(detail=False, methods=["post"], permission_classes=[])
    def search_car(self, request, *args, **kwargs):
        data = dict()
        for key, value in request.data.items():
            if key == 'csrfmiddlewaretoken':
                continue
            data[key] = value

        search_data = SearchBooking(**data)
        pick_up_lat, pick_up_long = search_data.pick_up_location_points()
        drop_off_lat, drop_off_long = search_data.drop_off_location_points()
        querystring = {"drop_off_datetime": search_data.drop_off_timestamp(),
                       "sort_by": request.data.get('sort_by', "recommended"),
                       "pick_up_datetime": search_data.pick_up_timestamp(),
                       "pick_up_latitude": pick_up_lat,
                       "from_country": request.data.get('from_country', "it"),
                       "locale": request.data.get('locale', "en-gb"),
                       "drop_off_latitude": drop_off_lat,
                       "drop_off_longitude": pick_up_long,
                       "pick_up_longitude": drop_off_long,
                       "currency": request.data.get('currency', "USD")
                       }

        headers = {
            'x-rapidapi-host': "booking-com.p.rapidapi.com",
            'x-rapidapi-key': "910e503bf3msh01b90ab3b1811d8p15372bjsn7670471df649"
        }

        response = requests.request("GET", self.api_url, headers=headers, params=querystring)

        if response.status_code == status.HTTP_200_OK:
            contex = json.loads(response.content)
            serialized_data = SearchSerializer(data=contex)
            if serialized_data.is_valid():
                return Response({'search_results': serialized_data.data.get('search_results')},
                                template_name='core/search.html',
                                status=status.HTTP_200_OK)
            else:
                return Response({'serializer': serialized_data.errors}, template_name='core/search_car.html',
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'content': response.content}, template_name='core/search_car.html',
                            status=response.status_code)
