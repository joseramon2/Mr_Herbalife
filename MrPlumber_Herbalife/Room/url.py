from django.urls import path
from Room.Views import views, viewCuartos
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('pisos/', views.PisosList.as_view()),
    path('pisos/<int:pk>', views.PisoNumero.as_view()),
    path('cuartos/', viewCuartos.CuartosGuardar.as_view()),
    path('cuartos/<int:pk2>', viewCuartos.CuartoList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)