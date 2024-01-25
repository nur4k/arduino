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
    transmitter_id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    direction = serializers.FloatField()
    speed = serializers.FloatField()
