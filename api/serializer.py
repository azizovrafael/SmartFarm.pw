from rest_framework import serializers
from .models import Arduino_Data


class Arduino_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Arduino_Data
        fields = '__all__'
