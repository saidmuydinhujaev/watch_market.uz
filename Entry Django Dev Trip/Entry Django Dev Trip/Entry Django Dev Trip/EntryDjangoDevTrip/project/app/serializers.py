from rest_framework import serializers
from .models import Watch

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = '__all__'