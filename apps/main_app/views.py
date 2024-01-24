from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.main_app.models import Item, Driver
from apps.main_app.serializers import GpsDataSerializer, ItemSerializer, DriverSerializer

from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from core.logger_settings import service_logger


class GpsDataView(APIView):
    serializer_class = GpsDataSerializer
    @csrf_exempt
    @swagger_auto_schema(request_body=GpsDataSerializer)
    def post(self, request):

        service_logger.info(f"Recive request with body --> {request.data}")
        # transmitter_id = request.POST.get('transmitter_id', '')
        # latitude = request.POST.get('latitude', '')
        # longitude = request.POST.get('longitude', '')
        # direction = request.POST.get('direction', '')
        # speed = request.POST.get('speed', '')
        
        # data_object = Item.objects.create(
        #     transmitter_id=transmitter_id,
        #     latitude=latitude,
        #     longitude=longitude,
        #     direction=direction,
        #     speed=speed
        # )
        # data_object.save()
        return Response("success")

class ItemView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DriverView(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
