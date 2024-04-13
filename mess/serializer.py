from rest_framework import serializers
from . import models

class MessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mess
        fields = "__all__"  # Include all fields from the model
