from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import Reportes, ActividadesRealizadas, ActividadAlerta
from Room.serializers import ReportesSerializer, ActividadesRealizadasSerializer,ActividadAlertaSerializer

class ReportesData(APIView):
    def post(self, request):
        reporte=Reportes()
        actR = ActividadesRealizadas()
        actAlrt = ActividadAlerta()
        try:
            reporte.creado= request.data["creado"]
            reporte.observaciones=request.data["observaciones"]
            reporte.inicio=request.data["inicio"]
            reporte.fin=request.data["fin"]
            reporte.cuarto_id=request.data["cuarto_id"]
            reporte.save()
            ##################
            actR.reporte_id=reporte.id
            for r in request.actividadesRealizadas:
                actR.observaciones=r.observaciones
                actR.realizado=r.realizado
                actR.accesorio_id=r.accerosio_id
                actR.actividades_id=r.actividades_id
            actR.save()
            ###################
            actAlrt.actividadRealizada_id=actR.id
            actAlrt.foco_id=request.data["foco_id"]
            ## Checar como lo manda Mario
            actAlrt.observaciones=request.data["ActAlert_observaciones"]##
            ##
            actAlrt.save()
        except Exception as e:
            print(e)
            raise Http404



    def get(self, request):

        return Response("{hola}", status=status.HTTP_200_OK)


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