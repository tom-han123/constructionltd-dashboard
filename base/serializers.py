from rest_framework import serializers
from .models import acc_register

class registerserializer(serializers.ModelSerializer):
    class Meta:
        model = acc_register
        fields = "__all__"

