from .models import Device,Room
from rest_framework import serializers


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    
    room = serializers.StringRelatedField(many=False)
    class Meta:
        model = Device
        fields = ('name', 'type', 'device_id', 'status','room')

