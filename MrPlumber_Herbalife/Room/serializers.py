from rest_framework import serializers
from Room.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

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
        model = Codigos
        fields = ('id', 'creado')

class AccesoriosActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccesoriosActividades
        fields = ('id', 'accesorio_id', 'actividades_id')

class FocosDeActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FocosDeActividad
        fields = ('id', 'colores', 'descripcion')

class ReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reportes
        fields=('id', 'creado_por', 'observaciones', 'inicio', 'fin', 'cuarto_id')

class ActividadesRealizadasSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActividadesRealizadas
        fields=('id', 'observaciones', 'realizado','accesorio_id', 'actividades_id', 'reporte_id')

class ActividadAlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActividadAlerta
        fields=('id','actividadRealizada_id','foco_id','observaciones')
