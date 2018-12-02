from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import Cuartos, Codigos
from Room.serializers import CuartosSerializer
from django.db import connection
import json
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def custom_query(id):
    if id is not None:
        with connection.cursor() as cursor:
            cursor.execute("SELECT "
            "Herbalife.Room_cuartos.id, "
            "Herbalife.Room_cuartos.nombre, "
            "Herbalife.Room_cuartos.descripcion, "
            "Herbalife.Room_cuartos.codigo_id, "
            "Herbalife.Room_cuartos.piso_id, "
            "Herbalife.Room_pisos.nombre AS \'piso_nombre\' "
            "FROM "
            "Herbalife.Room_cuartos "
            "INNER JOIN "
            "Herbalife.Room_pisos ON Herbalife.Room_cuartos.piso_id = Herbalife.Room_pisos.id "
            "WHERE "
            "Herbalife.Room_cuartos.codigo_id = %s;", [id])
            row = dictfetchall(cursor)
        return row

class CuartosGuardar(APIView):

    #renderer_classes = (JSONRenderer,)
    def get(self, request):
        query = request.GET.get("codigo")
        if query is None:
            dato = Cuartos.objects.all()
            serializer = CuartosSerializer(dato, many=True)
            return Response(serializer.data)
        else:
            dato=custom_query(int(query))#Cuartos.objects.get(codigo_id=int(query))
            #serializer=CuartosSerializer(dato)
            print(dato)
            if bool(dato):
                return Response(dato, status=status.HTTP_200_OK)
            else:
                data={'error':'no data'}
                return Response(data, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        print(request.data)
        dato = Cuartos()
        codigo= Codigos()
        codigo.save()
        print(codigo.id)
        if "nombre" in request.data:
            dato.nombre = request.data["nombre"]
        if "descripcion" in request.data:
            dato.descripcion = request.data["descripcion"]
        if "piso_id" in request.data:
            dato.piso_id = request.data["piso_id"]
        dato.codigo_id = codigo.id
        try:
            dato.save()
        except Exception as e:
            codigo.delete()
            dato={'confirmar': str(e)}
            return Response(dato , status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_201_CREATED)

class CuartoList(APIView):

    def get_object(self, pk2):
        try:
            res = Cuartos.objects.get(pk=pk2)
            return res
        except Cuartos.DoesNotExist:
            raise Http404

    def get(self, request, pk2):
        lista = self.get_object(pk2)
        serializer = CuartosSerializer(lista)
        return Response(serializer.data)

    def put(self, request, pk2):
        dato = self.get_object(pk2)
        datoAguardar = CuartosSerializer(dato, data=request.data)
        if datoAguardar.is_valid():
            datoAguardar.save()
            return Response(datoAguardar.data, status=status.HTTP_201_CREATED)
        return Response(datoAguardar.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk2):
        dato = self.get_object(pk2)
        serializer = CuartosSerializer(dato)
        dato.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
