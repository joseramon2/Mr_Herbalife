from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from Room.models import Reportes, ActividadesRealizadas, ActividadAlerta
#from Room.serializers import ReportesSerializer, ActividadesRealizadasSerializer,ActividadAlertaSerializer
from Room.Functions.fixDict import Fix
from django.utils import timezone
import pytz

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
                            "Herbalife.Room_reportes.id as \'reporte_id\', "
                            "Herbalife.Room_reportes.creado_por, "
                            "Herbalife.Room_reportes.observaciones as \'reporte_observaciones\', "
                            "Herbalife.Room_reportes.inicio, "
                            "Herbalife.Room_reportes.fin, "
                            "Herbalife.Room_reportes.cuarto_id, "
                            "Herbalife.Room_reportes.isReport, "
                            "Herbalife.Room_cuartos.nombre as \'cuarto_nombre\', "
                            "Herbalife.Room_cuartos.codigo_id as \'cuarto_codigo\', "
                            "Herbalife.Room_pisos.nombre as \'piso_nombre\', "
                            "Herbalife.Room_actividadesrealizadas.id as \'ActRealizada_id\', "
                            "Herbalife.Room_actividadesrealizadas.observaciones as 'ActRealizada_observaciones', "
                            "Herbalife.Room_actividadesrealizadas.realizado, "
                            "Herbalife.Room_actividadesrealizadas.accesorio_id, "
                            "Herbalife.Room_actividadesrealizadas.actividades_id, "
                            "Herbalife.Room_actividades.id as \'actividad_id\', "
                            "Herbalife.Room_actividades.nombre as \'actividad_nombre\', "
                            "Herbalife.Room_accesorios.nombre as \'accesorio_nombre\', "
                            "Herbalife.Room_actividadalerta.id \'ActAlert_id\', "
                            "Herbalife.Room_actividadalerta.observaciones as \'ActAlerta_observaciones\', "
                            "Herbalife.Room_actividadalerta.foco_id, "
                            "Herbalife.Room_focosdeactividad.colores, "
                            "Herbalife.Room_focosdeactividad.descripcion "
                        "FROM "
                            "Herbalife.Room_reportes "
                                "inner join "
                                    "Herbalife.Room_cuartos on Herbalife.Room_reportes.cuarto_id = Herbalife.Room_cuartos.id "
                                "inner join "
                                    "Herbalife.Room_actividadesrealizadas on Herbalife.Room_actividadesrealizadas.reporte_id = Herbalife.Room_reportes.id "
                                "inner join "
                                    "Herbalife.Room_actividades on Herbalife.Room_actividades.id = Herbalife.Room_actividadesrealizadas.actividades_id "
                                "inner join "
                                    "Herbalife.Room_actividadalerta on Herbalife.Room_actividadalerta.actividadRealizada_id = Herbalife.Room_actividadesrealizadas.id "
                                "inner join "
                                    "Herbalife.Room_accesorios on Herbalife.Room_actividadesrealizadas.accesorio_id = Herbalife.Room_accesorios.id "
                                "inner join "
                                    "Herbalife.Room_focosdeactividad on Herbalife.Room_focosdeactividad.id = Herbalife.Room_actividadalerta.foco_id "
                                "inner join "
                                    "Herbalife.Room_pisos on Herbalife.Room_cuartos.piso_id = Herbalife.Room_pisos.id "
                           "order by Herbalife.Room_reportes.id;")
            row = dictfetchall(cursor)
        return row
    elif id > 0:
        with connection.cursor() as cursor:
            cursor.execute("SELECT "
                            "Herbalife.Room_reportes.id as \'reporte_id\', "
                            "Herbalife.Room_reportes.creado_por, "
                            "Herbalife.Room_reportes.observaciones as \'reporte_observaciones\', "
                            "Herbalife.Room_reportes.inicio, "
                            "Herbalife.Room_reportes.fin, "
                            "Herbalife.Room_reportes.cuarto_id, "
                            "Herbalife.Room_reportes.isReport, "
                            "Herbalife.Room_cuartos.nombre as \'cuarto_nombre\', "
                            "Herbalife.Room_cuartos.codigo_id as \'cuarto_codigo\', "
                            "Herbalife.Room_pisos.nombre as \'piso_nombre\', "
                            "Herbalife.Room_actividadesrealizadas.id as \'ActRealizada_id\', "
                            "Herbalife.Room_actividadesrealizadas.observaciones as \'ActRealizada_observaciones\', "
                            "Herbalife.Room_actividadesrealizadas.realizado, "
                            "Herbalife.Room_actividadesrealizadas.accesorio_id, "
                            "Herbalife.Room_actividadesrealizadas.actividades_id, "
                            "Herbalife.Room_actividades.id as \'actividad_id\', "
                            "Herbalife.Room_actividades.nombre as \'actividad_nombre\', "
                            "Herbalife.Room_accesorios.nombre as \'accesorio_nombre\', "
                            "Herbalife.Room_actividadalerta.id \'ActAlert_id\', "
                            "Herbalife.Room_actividadalerta.observaciones as \'ActAlerta_observaciones\', "
                            "Herbalife.Room_actividadalerta.foco_id, "
                            "Herbalife.Room_focosdeactividad.colores, "
                            "Herbalife.Room_focosdeactividad.descripcion "
                        "FROM "
                            "Herbalife.Room_reportes "
                                "inner join "
                                    "Herbalife.Room_cuartos on Herbalife.Room_reportes.cuarto_id = Herbalife.Room_cuartos.id "
                                "inner join "
                                    "Herbalife.Room_actividadesrealizadas on Herbalife.Room_actividadesrealizadas.reporte_id = Herbalife.Room_reportes.id "
                                "inner join "
                                    "Herbalife.Room_actividades on Herbalife.Room_actividades.id = Herbalife.Room_actividadesrealizadas.actividades_id "
                                "inner join "
                                    "Herbalife.Room_actividadalerta on Herbalife.Room_actividadalerta.actividadRealizada_id = Herbalife.Room_actividadesrealizadas.id "
                                "inner join "
                                    "Herbalife.Room_accesorios on Herbalife.Room_actividadesrealizadas.accesorio_id = Herbalife.Room_accesorios.id "
                                "inner join "
                                    "Herbalife.Room_focosdeactividad on Herbalife.Room_focosdeactividad.id = Herbalife.Room_actividadalerta.foco_id "
                                "inner join "
                                    "Herbalife.Room_pisos on Herbalife.Room_cuartos.piso_id = Herbalife.Room_pisos.id "
                        "where Herbalife.Room_reportes.id=%s "
                           "order by Herbalife.Room_reportes.id;", [id])
            row = dictfetchall(cursor)
        return row

class ReportesData(APIView):



    def post(self, request):
        reporte=Reportes()
        print("request")
        print(request.data)
        print("end request")
        try:
            reporte.creado_por= request.data["creado_por"]
            reporte.observaciones=request.data["observaciones"]
            reporte.inicio=request.data["inicio"]
            reporte.fin=request.data["fin"]
            reporte.cuarto_id=request.data["cuarto_id"]
            print(request.data["isReport"])
            reporte.isReport = request.data["isReport"]
            reporte.save()
            ##################

            for r in request.data["actividadesRealizadas"]:
                print("\n")
                #print(r)
                actR = ActividadesRealizadas()
                print("ACTREAL_ID: "+str(actR.id)+"\n")
                actR.reporte_id = reporte.id
                actR.observaciones=r["observaciones"]
                print("\n"+r["realizado"])
                actR.realizado= r["realizado"]
                actR.accesorio_id=r["accesorio_id"]
                actR.actividades_id=r["actividades_id"]
                print("\n")
                actR.save()
                print("ACTREAL_ID: " + str(actR.id) + "\n")
            ###################
                actAlrt = ActividadAlerta()
                actAlrt.actividadRealizada_id=actR.id
                actAlrt.foco_id=r["foco_id"]
            ## Checar como lo manda Mario
                actAlrt.observaciones=request.data["ActAlerta_observaciones"]##
            ##
                actAlrt.save()
            print(request.data)
            return Response({"ok":"Reporte creado"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("############################")
            print(e)
            #reporte.delete()
            return Response({"error":str(e)}, status=status.HTTP_204_NO_CONTENT)



    def get(self, request):
        dato = my_custom_sql()
        FixObjt= Fix()
        return Response(FixObjt.fixDict_(dato), status=status.HTTP_200_OK)


class ReportesInfo(APIView):
    def get_object(self, pk):
        try:
            dato=Reportes.objects.get(pk=pk)
            return dato
        except Reportes.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        #dato=self.get_object(pk)
        #serializer = ReportesSerializer(dato)
        FixObjt = Fix()
        dato=my_custom_sql(pk)
        return Response(FixObjt.fixDict_(dato), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        dato=self.get_object(pk)
        dato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReporteEditDesc(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def put(self, request):
        try:
            '''ActRea = ActividadesRealizadas.objects.get(id=1)
            print("\n\n")
            print(ActRea.realizado)
            reporte = ActividadesRealizadas.objects.get(pk=request.data["ActRealizada_id"])
            reporte.observaciones=request.data["ActRealizada_observaciones"]
            reporte.save()

            actAlert = ActividadAlerta.objects.get(pk=request.data["ActAlert_id"])
            actAlert.foco_id=request.data["foco_id"]
            print("\n\n")
            #print(actAlert.realizado)
            actAlert.save()
            #print(actAlert.realizado)
            print("\n\n")
            print("\n\n")
            print(ActRea.realizado)'''
            print(update(request.data["ActRealizada_id"], request.data["ActRealizada_observaciones"], request.data["ActAlert_id"], request.data["foco_id"]))

            return Response({"Mensaje": "Ok"}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


class ReporteUltimoQuery(APIView):
    def get(self, request):
        return Response(ultimoDato(), status=status.HTTP_200_OK)


def update(ActRealizada_id, ActRealizada_observaciones, ActAlert_id, foco_id):
    with connection.cursor() as cursor:
        cursor.execute("Update Herbalife.Room_actividadesrealizadas set observaciones=%s where id=%s;", [ActRealizada_observaciones, ActRealizada_id])
        cursor.execute("Update Herbalife.Room_actividadalerta set foco_id=%s where id=%s;", [foco_id, ActAlert_id])
        print("update")
        row = cursor.fetchone()
    return row

def ultimoDato():
    with connection.cursor() as cursor:
        cursor.execute(
                        "SELECT "
                        "Room_accesorios.nombre, "
                        "Room_accesorios.codigo_id, "
                        "Room_cuartos.nombre AS \'cuarto\', "
                        "Room_pisos.nombre AS \'piso\', "
                        "Room_actividadesrealizadas.observaciones, "
                        "Room_actividadesrealizadas.realizado, "
                        "Room_focosdeactividad.colores, "
                        "Room_focosdeactividad.descripcion "
                        "FROM "
                        "Room_actividadesrealizadas "
                        "INNER JOIN "
                        "Room_accesorios ON Room_accesorios.id = Room_actividadesrealizadas.accesorio_id "
                        "INNER JOIN "
                        "Room_actividadalerta ON Room_actividadalerta.actividadRealizada_id = Room_actividadesrealizadas.id "
                        "INNER JOIN "
                        "Room_focosdeactividad ON Room_focosdeactividad.id = Room_actividadalerta.foco_id "
                        "INNER JOIN "
                        "Room_cuartos ON Room_cuartos.id = Room_accesorios.cuarto_id "
                        "INNER JOIN "
                        "Room_pisos ON Room_pisos.id = Room_cuartos.piso_id "
                        "WHERE "
                        "Room_actividadesrealizadas.id IN (SELECT " 
                        "MAX(id) AS \'id\' " 
                        "FROM "
                        "Room_actividadesrealizadas "
                        "GROUP BY Room_actividadesrealizadas.accesorio_id) "
                        "ORDER BY piso DESC "
                            )
        row = dictfetchall(cursor)
    return row
'''
{
"ActRealizada_id": 11,
"ActRealizada_observaciones": "jojojojojojo",
"ActAlert_id": 11
"foco_id": 82585858
}
'''