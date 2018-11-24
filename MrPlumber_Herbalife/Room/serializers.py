from rest_framework import serializers
from Room.models import *


class PisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pisos
        fields = ('id', 'nombre', 'descripcion')

class CuartosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuartos
        fields = ('id', 'nombre', 'descripcion', 'codigo_id', 'piso_id')

class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = ('id', 'nombre', 'descripcion')

class AccesoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesorios
        fields = ('id', 'nombre', 'descripcion','cuarto_id', 'codigo_id')

class CodigosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'creado')