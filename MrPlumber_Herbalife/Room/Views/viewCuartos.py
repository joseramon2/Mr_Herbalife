from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import Cuartos
from Room.serializers import CuartosSerializer
from django.db import connection


'''
    De acuerto a la doc de Django, hay que utilizar esas 2 funciones; 
    nos combierten el query a Diccionario (que es necesario para usar Json)
    [{'id': 1, 'nombre': 'ddd', 'descripcion': 'dddd', 'codigo_id': None, 'piso_id': 1}, {'id': 2, 'nombre': 'bbbb', 'descripcion': 'bbb', 'codigo_id': None, 'piso_id': 1}]

'''
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def my_custom_sql(num):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Room_cuartos where id= %s;", [num])
        row = dictfetchall(cursor)
    return row

class CuartosGuardar(APIView):
    def post(self, request):
        datoGuardar = CuartosSerializer(data=request.data)
        if datoGuardar.is_valid():
            datoGuardar.save()
            return Response(datoGuardar.data, status=status.HTTP_201_CREATED)
        return Response(datoGuardar.errors, status=status.HTTP_400_BAD_REQUEST)

class CuartoList(APIView):

    def get_object(self, pk2):

        try:

            res = my_custom_sql(pk2)#Cuartos.objects.raw("Select * from Room_cuartos where id=1;")#get(pk=pk2)
            if len(res) == 0:
                raise Http404
            else:
                return res
        except Cuartos.DoesNotExist:
            raise Http404

    def get(self, request, pk2):
        lista = self.get_object(pk2)
        #

        #
        if len(lista) > 1:
            serializer = CuartosSerializer(lista, many=True)
        else:
            serializer = CuartosSerializer(lista[0])
        return Response(serializer.data)