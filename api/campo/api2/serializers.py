from rest_framework import serializers
from campo import models

class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Campo
        fields = '__all__'