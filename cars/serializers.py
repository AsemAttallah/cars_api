from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta :
        model = Car
        # fields = ['purchaser','type','desc']
        fields='__all__'