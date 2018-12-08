from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import Reportes, ActividadesRealizadas, ActividadAlerta
from Room.serializers import ReportesSerializer, ActividadesRealizadasSerializer,ActividadAlertaSerializer

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
            cursor.execute(";")
            row = dictfetchall(cursor)
        return row
    elif id > 0:
        with connection.cursor() as cursor:
            cursor.execute(";", [id])
            row = dictfetchall(cursor)
        return row

class ReportesData(APIView):



    def post(self, request):
        reporte=Reportes()
        print(request.data)

        try:
            reporte.creado_por= request.data["creado_por"]
            reporte.observaciones=request.data["observaciones"]
            reporte.inicio=request.data["inicio"]
            reporte.fin=request.data["fin"]
            reporte.cuarto_id=request.data["cuarto_id"]
            reporte.save()
            ##################

            for r in request.data["actividadesRealizadas"]:
                print("\n")
                print(r)
                actR = ActividadesRealizadas()
                actR.reporte_id = reporte.id
                actR.observaciones=r["observaciones"]
                actR.realizado=r["realizado"]
                actR.accesorio_id=r["accesorio_id"]
                actR.actividades_id=r["actividades_id"]
                print("\n")
                actR.save()
            ###################
                actAlrt = ActividadAlerta()
                actAlrt.actividadRealizada_id=actR.id
                actAlrt.foco_id=r["foco_id"]
            ## Checar como lo manda Mario
                actAlrt.observaciones=request.data["ActAlerta_observaciones"]##
            ##
                actAlrt.save()
            return Response({"ok":"Reporte creado"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("############################")
            print(e)
            #reporte.delete()
            return Response({"error":str(e)})



    def get(self, request):

        return Response("{\"hola\":\"adios\"}", status=status.HTTP_200_OK)


class ReportesInfo(APIView):
    def get_object(self, pk):
        try:
            dato=Reportes.objects.get(pk=pk)
            return dato
        except Reportes.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dato=self.get_object(pk)
        serializer = ReportesSerializer(dato)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        dato=self.get_object(pk)
        dato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
{
  "codigoRoom": 2,
  "inicio": "",
  "fin": "",
  "observaciones": "",
  "actividadesRealizadas": [
    {
      "codigoAccesorio": 2,
      "idActividad": 1,
      "observacion": "",
      "idFoco": 1,
      "hora": ""
    }
  ]
}
'''