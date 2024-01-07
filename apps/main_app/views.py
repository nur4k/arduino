from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.main_app.models import Item, Driver
from apps.main_app.serializers import ItemSerializer, DriverSerializer


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from core.logger_settings import service_logger

@csrf_exempt
def handle_data(request):
    if request.method == 'POST':
        service_logger.info(f"Recive request with body --> {request.POST}")
        transmitter_id = request.POST.get('transmitter_id', '')
        latitude = request.POST.get('latitude', '')
        longitude = request.POST.get('longitude', '')
        direction = request.POST.get('direction', '')
        speed = request.POST.get('speed', '')

        try:
            data_object = Item.objects.create(
                transmitter_id=transmitter_id,
                latitude=latitude,
                longitude=longitude,
                direction=direction,
                speed=speed
            )
            data_object.save()

            return HttpResponse('Data received and saved successfully')
        except Exception as e:
            return HttpResponse(f'Error: {e}')

    return HttpResponse('Invalid request method')

class ItemView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DriverView(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
