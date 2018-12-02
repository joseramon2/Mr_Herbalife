from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import AccesoriosActividades
from Room.serializers import AccesoriosActividadesSerializer
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
            cursor.execute("SELECT "
                           "Herbalife.Room_accesoriosactividades.id ,"
                           "Herbalife.Room_accesorios.id as \'accesorio_id\' ,"
                           "Herbalife.Room_accesorios.nombre as \'accesorio_nombre\' ,"
                           "Herbalife.Room_actividades.id as \'actividad_id\' ,"
                           "Herbalife.Room_actividades.nombre as \'actividad_nombre\' "
                           "FROM "
                           "Herbalife.Room_accesoriosactividades "
                           "INNER JOIN "
                           "Herbalife.Room_accesorios ON Herbalife.Room_accesorios.id = Herbalife.Room_accesoriosactividades.accesorio_id "
                           "INNER JOIN "
                           "Herbalife.Room_actividades ON Herbalife.Room_actividades.id = Herbalife.Room_accesoriosactividades.actividades_id;")
            row = dictfetchall(cursor)
        return row
    elif id > 0:
        with connection.cursor() as cursor:
            cursor.execute("SELECT "
                           "Herbalife.Room_accesoriosactividades.id ,"
                           "Herbalife.Room_accesorios.id as \'accesorio_id\' ,"
                           "Herbalife.Room_accesorios.nombre as \'accesorio_nombre\' ,"
                           "Herbalife.Room_actividades.id as \'actividad_id\' ,"
                           "Herbalife.Room_actividades.nombre as \'actividad_nombre\' "
                           "FROM "
                           "Herbalife.Room_accesoriosactividades "
                           "INNER JOIN "
                           "Herbalife.Room_accesorios ON Herbalife.Room_accesorios.id = Herbalife.Room_accesoriosactividades.accesorio_id "
                           "INNER JOIN "
                           "Herbalife.Room_actividades ON Herbalife.Room_actividades.id = Herbalife.Room_accesoriosactividades.actividades_id "
                           "WHERE Herbalife.Room_accesoriosactividades.id =%s;", [id])
            row = dictfetchall(cursor)
        return row


class AltaActividad(APIView):
    def get(self, request):
        dato = my_custom_sql()#AccesoriosActividades.objects.all()
        #serializer = AccesoriosActividadesSerializer(dato, many=True)
        return Response(dato)

    def post(self, request):
        # dato = AccesoriosActividadesSerializer(data=request.data)
        dato2 = AccesoriosActividades()
        print(request.data['accesorio_id'])
        dato2.accesorio_id = request.data['accesorio_id']
        dato2.actividades_id = request.data['actividades_id']
        print(dato2.accesorio_id)
        print("##########################")

        try:
            dato2.save()
            serializer = AccesoriosActividadesSerializer(dato2)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Actividad(APIView):
    def get_object(self, pk):
        try:
            return AccesoriosActividades.objects.get(pk=pk)
        except AccesoriosActividades.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dato = my_custom_sql(pk)
        if len(dato) ==0:
            return Response("{\"nada\"}", status=status.HTTP_204_NO_CONTENT)
        return Response(dato)

    def put(self, request, pk):
        detalle = self.get_object(pk)
        print("###############################")
        print(detalle.accesorio_id)
        detalle.accesorio_id = request.data['accesorio_id']
        detalle.actividades_id = request.data['actividades_id']
        dato = AccesoriosActividadesSerializer(detalle)
        try:
            detalle.save()
            dato = AccesoriosActividadesSerializer(detalle)
            return Response(dato.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dato = self.get_object(pk)
        mostrar = AccesoriosActividadesSerializer(dato)
        dato.delete()
        return Response(mostrar.data, status=status.HTTP_204_NO_CONTENT)