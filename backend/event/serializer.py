from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    """Event."""

    class Meta:
        """Meta Class."""

        model = Event
        fields = ('full_name', 'mobile', 'email', 'idCard', 'type', 'tickets')
