from rest_framework import viewsets
from campo.api2 import serializers
from campo import models

class CampoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CampoSerializer
    queryset = models.Campo.objects.all()
