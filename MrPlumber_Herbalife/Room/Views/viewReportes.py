from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import Reportes, ActividadesRealizadas, ActividadAlerta
from Room.serializers import ReportesSerializer, ActividadesRealizadasSerializer,ActividadAlertaSerializer

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
                actAlrt.foco_id=request.data["foco_id"]
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
    def get(self, request, pk):
        return Response(status=status.HTTP_200_OK)
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