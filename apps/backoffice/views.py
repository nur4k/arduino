from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.backoffice.models import GIS, Driver
from apps.backoffice.serializers import (
    DriverSerializer,
    GisSerializer,
    GpsDataSerializer,
)
from core.logger_settings import service_logger


class GpsDataView(APIView):
    serializer_class = GpsDataSerializer

    @csrf_exempt
    @swagger_auto_schema(request_body=GpsDataSerializer)
    def post(self, request: Request) -> Response:
        service_logger.info(f"Recive request with body --> {request.data}")
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        GIS.objects.create(**serializer.validated_data)
        return Response("success")


class GisView(ModelViewSet):
    queryset = GIS.objects.all()
    serializer_class = GisSerializer


class DriverView(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
