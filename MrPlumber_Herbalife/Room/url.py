from django.urls import path
from Room.Views import views, viewCuartos, viewActividades, viewAccesoriosDeBanos, viewAltaActividad, viewFocosDeActividad, viewReportes
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('pisos/', views.PisosList.as_view()),
    path('pisos/<int:pk>', views.PisoNumero.as_view()),
    path('cuartos/', viewCuartos.CuartosGuardar.as_view()),
    path('cuartos/<int:pk2>', viewCuartos.CuartoList.as_view()),
    path('actividades/', viewActividades.InsertarActividad.as_view()),
    path('actividades/<int:pk>', viewActividades.EditarActividad.as_view()),
    path('accesorios/', viewAccesoriosDeBanos.InsertarAccesorio.as_view()),
    path('accesorios/<int:pk>', viewAccesoriosDeBanos.listAccesorios.as_view()),
    path('accesorios/listaActividades/<int:pk>', viewAccesoriosDeBanos.listaActividades.as_view()),
    path('accesorioActividad/', viewAltaActividad.AltaActividad.as_view()),
    path('accesorioActividad/<int:pk>', viewAltaActividad.Actividad.as_view()),
    path('alertas/', viewFocosDeActividad.focoActividad.as_view()),
    path('alertas/<int:pk>', viewFocosDeActividad.focoActividadInfo.as_view()),
    path('reportes/', viewReportes.ReportesData.as_view()),
    path('reportes/<int:pk>', viewReportes.ReportesInfo.as_view()),
    path('cuartos/accesorios/<int:pk2>', viewCuartos.CuartoAccesorios.as_view()),
    path('actividad/reporte/', viewReportes.ReporteEditDesc.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)