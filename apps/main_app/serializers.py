from rest_framework import serializers

from apps.main_app.models import Item, Driver


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'transmitter_id','latitude', 'longitude', 'direction', 'speed', 'timestamp', 'driver')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'fio', 'car_number')
