from rest_framework import serializers

from apps.backoffice.models import GIS, Driver


class GisSerializer(serializers.ModelSerializer):
    class Meta:
        model = GIS
        fields = (
            "id",
            "transmitter_id",
            "latitude",
            "longitude",
            "direction",
            "speed",
            "timestamp",
            "driver",
        )


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ("id", "fio", "car_number")


class GpsDataSerializer(serializers.Serializer):
    transmitter_id = serializers.FloatField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    direction = serializers.FloatField()
    speed = serializers.FloatField()
    {
        "transmitter_id": 1,
        "latitude": 41.41,
        "longitude": 72.43,
        "direction": 0,
        "speed": 0,
    }
