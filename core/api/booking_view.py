import json

import requests
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.models.booking import SearchBooking
from core.serializers.search_serializer import SearchSerializer
from utils.content_manager import get_errors


class VehicleViewSet(ViewSet):
    api_url = "https://booking-com.p.rapidapi.com/v1/car-rental/"
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    @action(detail=False, methods=["post"], permission_classes=[])
    def search(self, request, *args, **kwargs):
        self.api_url = self.api_url + "search"
        data = dict()
        for key, value in request.data.items():
            if key == 'csrfmiddlewaretoken':
                continue
            data[key] = value
        search_data = SearchBooking(**data)
        response = requests.request(
            method="GET",
            url=self.api_url,
            headers=SearchBooking.get_headers(),
            params=search_data.get_query_params(request)
        )

        if response.status_code == status.HTTP_200_OK:
            contex = json.loads(response.content)
            serialized_data = SearchSerializer(data=contex)
            if serialized_data.is_valid():
                return Response({'search_results': serialized_data.data.get('search_results'),
                                 'search_key': serialized_data.data.get('search_key')},
                                template_name='core/cars.html',
                                status=status.HTTP_200_OK)
            else:
                content = json.loads(serialized_data.errors)
                messages.error(request, content, 'danger')
                return redirect('search')
        else:
            try:
                content = get_errors(json.loads(response.content))
                messages.error(request, content, 'danger')
                return redirect('search')
            except:
                messages.error(request, response.content, 'danger')
                return redirect('search')


class VehicleDetail(View):
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    api_url = "https://booking-com.p.rapidapi.com/v1/car-rental/"

    def get(self, request, *args, **kwargs):
        self.api_url = self.api_url + "detail"
        response = requests.request(
            method="GET",
            url=self.api_url,
            headers=SearchBooking.get_headers(),
            params={
                "vehicle_id": kwargs.get('vehicle_id'),
                "search_key": kwargs.get('search_key', None),
                "from_country": request.GET.get('from_country', "it"),
                "locale": request.GET.get('locale', "en-gb"),
                "currency": request.GET.get('currency', "USD")
            }
        )

        if response.status_code == 200:
            json_data = json.loads(response.content)
            return render(request, 'core/car-single.html', {'vehicle': json_data.get('vehicle')})
        else:
            messages.error(response.content, 'danger')
            return redirect('search')
