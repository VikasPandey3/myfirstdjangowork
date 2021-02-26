from rest_framework import serializers
from .models import Iot


class IotSerializers(serializers.ModelSerializer):

    class Meta:
        model = Iot
        fields = ('pin_no', 'state', 'id')
