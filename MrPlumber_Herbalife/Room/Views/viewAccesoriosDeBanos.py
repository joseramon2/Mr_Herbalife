from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import Accesorios
from Room.serializers import AccesoriosSerializer
from django.db import connection

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def my_custom_sql(id=None):
    if id is None:
        with connection.cursor() as cursor:
            cursor.execute("SELECT Herbalife.Room_accesorios.id, Herbalife.Room_accesorios.nombre, Herbalife.Room_accesorios.descripcion, Herbalife.Room_cuartos.id as \"Cuarto_ID\", Herbalife.Room_cuartos.nombre as \"Cuarto_Nombre\", Herbalife.Room_cuartos.descripcion as \"Cuarto_Descripcion\", Herbalife.Room_pisos.id as \"Piso_ID\", Herbalife.Room_pisos.nombre as \"Piso_Nombre\", Herbalife.Room_pisos.descripcion as \"Piso_Descripcion\" From Herbalife.Room_accesorios Inner Join Herbalife.Room_cuartos on Herbalife.Room_accesorios.cuarto_id=Herbalife.Room_cuartos.id inner Join Herbalife.Room_pisos on Herbalife.Room_cuartos.piso_id = Herbalife.Room_pisos.id;")
            row = dictfetchall(cursor)
        return row
    elif id >=0:
        with connection.cursor() as cursor:
            cursor.execute("SELECT Herbalife.Room_accesorios.id, Herbalife.Room_accesorios.nombre, Herbalife.Room_accesorios.descripcion, Herbalife.Room_cuartos.id as \"Cuarto_ID\", Herbalife.Room_cuartos.nombre as \"Cuarto_Nombre\", Herbalife.Room_cuartos.descripcion as \"Cuarto_Descripcion\", Herbalife.Room_pisos.id as \"Piso_ID\", Herbalife.Room_pisos.nombre as \"Piso_Nombre\", Herbalife.Room_pisos.descripcion as \"Piso_Descripcion\" From Herbalife.Room_accesorios Inner Join Herbalife.Room_cuartos on Herbalife.Room_accesorios.cuarto_id=Herbalife.Room_cuartos.id inner Join Herbalife.Room_pisos on Herbalife.Room_cuartos.piso_id = Herbalife.Room_pisos.id WHERE Herbalife.Room_cuartos.id =%s;", [id])
            row = dictfetchall(cursor)
        return row

class InsertarAccesorio(APIView):

    def post(self, request):
        print(request.data)
        dato = Accesorios()
        try:
            for value in request.data:
                print(value, ":", request.data[value])
                if value =="nombre":
                    dato.nombre=request.data[value]
                elif value =="descripcion":
                    dato.descripcion=request.data[value]
                elif value =="cuarto_id":
                    dato.cuarto_id=request.data[value]
                elif value == "id":
                    try:
                        #"{\"response\":\"id diplucado\"}",
                        aux = Accesorios.objects.get(id=request.data[value])
                        return Response("{\"response\":\"id diplucado\"}",status=status.HTTP_400_BAD_REQUEST)
                    except Accesorios.DoesNotExist:
                        dato.id = request.data[value]
                elif value =="codigo_id":
                    dato.codigo_id=request.data[value]
            dato.save()
            return Response(status=status.HTTP_201_CREATED)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):

        query = request.GET.get('cuarto')
        if query is None:
            dato = my_custom_sql()
            print("############")
            print(query)
            return Response(dato, status=status.HTTP_200_OK)
        else:
            dato = my_custom_sql(int(query))
            print("############")
            print(query)
            return Response(dato, status=status.HTTP_200_OK)
        #print(dato)
        #serializer = AccesoriosSerializer(dato)


class listAccesorios(APIView):

    def get_object(self, pk):
        try:
            return Accesorios.objects.get(pk=pk)
        except Accesorios.DoesNotExist:
            raise Http404


    def get(self, request, pk,format=None):
        dato = self.get_object(pk)
        serializer = AccesoriosSerializer(dato)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        detalle = self.get_object(pk)
        valorAGuardar = AccesoriosSerializer(detalle, data=request.data)
        if valorAGuardar.is_valid():
            valorAGuardar.save()
            return Response(valorAGuardar.data, status=status.HTTP_200_OK)
        return Response(valorAGuardar.errors, status=status.HTTP_400_BAD_REQUEST)





















        '''
        SELECT
        Herbalife.Room_accesorios.id, Herbalife.Room_accesorios.nombre, Herbalife.Room_accesorios.descripcion,
        Herbalife.Room_cuartos.id as "Cuarto_ID", Herbalife.Room_cuartos.nombre as "Cuarto_Nombre", Herbalife.Room_cuartos.descripcion as "Cuarto_Descripcion",
        Herbalife.Room_pisos.id as "Piso_ID", Herbalife.Room_pisos.nombre as "Piso_Nombre", Herbalife.Room_pisos.descripcion as "Piso_Descripcion"
        From Herbalife.Room_accesorios
        Inner Join Herbalife.Room_cuartos on Herbalife.Room_accesorios.cuarto_id=Herbalife.Room_cuartos.id
        inner Join Herbalife.Room_pisos on Herbalife.Room_cuartos.piso_id = Herbalife.Room_pisos.id;
        :param request:
        :return:
        '''