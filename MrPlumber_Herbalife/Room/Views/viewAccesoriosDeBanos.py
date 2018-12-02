from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import Accesorios, Codigos
from Room.serializers import AccesoriosSerializer
from django.db import connection

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def codigo_query(codigo):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT Herbalife.Room_accesorios.id, Herbalife.Room_accesorios.nombre, Herbalife.Room_accesorios.descripcion, Herbalife.Room_cuartos.id as"
            " \"cuarto_ID\", Herbalife.Room_cuartos.nombre as \"cuarto_Nombre\", Herbalife.Room_cuartos.descripcion as \"cuarto_descripcion\", Herbalife.Room_pisos.id as "
            "\"piso_ID\", Herbalife.Room_pisos.nombre as \"piso_Nombre\", Herbalife.Room_pisos.descripcion as \"piso_descripcion\" ,"
            "Herbalife.Room_codigos.id as \"codigo\" "
            "From Herbalife.Room_accesorios "
            "Inner Join Herbalife.Room_cuartos on Herbalife.Room_accesorios.cuarto_id=Herbalife.Room_cuartos.id "
            "inner Join Herbalife.Room_pisos on Herbalife.Room_cuartos.piso_id = Herbalife.Room_pisos.id "
            "Inner Join Herbalife.Room_codigos on Herbalife.Room_accesorios.codigo_id = Herbalife.Room_codigos.id "
            "WHERE Herbalife.Room_accesorios.codigo_id =%s;", [codigo])
        row = dictfetchall(cursor)
    return row

def my_custom_sql(id=None):
    if id is None:
        with connection.cursor() as cursor:
            cursor.execute("SELECT Herbalife.Room_accesorios.id, Herbalife.Room_accesorios.nombre, Herbalife.Room_accesorios.descripcion, Herbalife.Room_cuartos.id as"
                           " \"cuarto_ID\", Herbalife.Room_cuartos.nombre as \"cuarto_Nombre\", Herbalife.Room_cuartos.descripcion as \"cuarto_descripcion\", Herbalife.Room_pisos.id as "
                           "\"piso_ID\", Herbalife.Room_pisos.nombre as \"piso_Nombre\", Herbalife.Room_pisos.descripcion as \"piso_descripcion\" ,"
                           "Herbalife.Room_codigos.id as \"codigo\" "
                           "From Herbalife.Room_accesorios "
                           "Inner Join Herbalife.Room_cuartos on Herbalife.Room_accesorios.cuarto_id=Herbalife.Room_cuartos.id "
                           "inner Join Herbalife.Room_pisos on Herbalife.Room_cuartos.piso_id = Herbalife.Room_pisos.id "
                           "Inner Join Herbalife.Room_codigos on Herbalife.Room_accesorios.codigo_id = Herbalife.Room_codigos.id;")
            row = dictfetchall(cursor)
        return row
    elif id >=0:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT Herbalife.Room_accesorios.id, Herbalife.Room_accesorios.nombre, Herbalife.Room_accesorios.descripcion, Herbalife.Room_cuartos.id as"
                " \"cuarto_ID\", Herbalife.Room_cuartos.nombre as \"cuarto_Nombre\", Herbalife.Room_cuartos.descripcion as \"cuarto_descripcion\", Herbalife.Room_pisos.id as "
                "\"piso_ID\", Herbalife.Room_pisos.nombre as \"piso_Nombre\", Herbalife.Room_pisos.descripcion as \"piso_descripcion\" ,"
                "Herbalife.Room_codigos.id as \"codigo\" "
                "From Herbalife.Room_accesorios "
                "Inner Join Herbalife.Room_cuartos on Herbalife.Room_accesorios.cuarto_id=Herbalife.Room_cuartos.id "
                "inner Join Herbalife.Room_pisos on Herbalife.Room_cuartos.piso_id = Herbalife.Room_pisos.id "
                "Inner Join Herbalife.Room_codigos on Herbalife.Room_accesorios.codigo_id = Herbalife.Room_codigos.id "
                "WHERE Herbalife.Room_cuartos.id =%s;", [id])
            row = dictfetchall(cursor)
        return row

class InsertarAccesorio(APIView):

    def post(self, request):
        dato = Accesorios()
        codigo = Codigos()
        codigo.save()
        if "nombre" in request.data:
            dato.nombre=request.data["nombre"]
        if "descripcion" in request.data:
            dato.descripcion=request.data["descripcion"]
        if "cuarto_id" in request.data:
            dato.cuarto_id=request.data["cuarto_id" ]
        dato.codigo_id=codigo.id
        try:
            dato.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            codigo.delete()

            data={'error':str(e)}
            return Response(data, status=status.HTTP_404_NOT_FOUND)


    def get(self, request):
        query=0
        query2=0
        try:
            query = request.GET.get('cuarto')
            query2= request.GET.get("codigo")
            if query is not None:
                dato = my_custom_sql(int(query))
                if bool(dato):
                    return Response(dato, status=status.HTTP_200_OK)
                else:
                    return Response({'detalle': 'no hay datos'}, status=status.HTTP_204_NO_CONTENT)
            elif query2 is not None:
                dato=codigo_query(int(query2))
                if bool(dato):
                    return Response(dato, status=status.HTTP_200_OK)
                else:
                    return Response({'detalle': 'no hay datos'}, status=status.HTTP_204_NO_CONTENT)
            else:
                dato = Accesorios.objects.all()
                serializer=AccesoriosSerializer(dato, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            print(e)
            #data={'error':str(e)}
            #return Response(data, status=status.HTTP_400_BAD_REQUEST)
            raise Http404

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

    def delete(self, request, pk, format=None):
        dato = self.get_object(pk)
        mostrar = AccesoriosSerializer(dato)
        dato.delete()
        return Response(mostrar.data, status=status.HTTP_204_NO_CONTENT)
