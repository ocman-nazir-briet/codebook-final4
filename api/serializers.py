from base.models import *
from rest_framework import serializers

class RoomSerial(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
class MessageSerial(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
