from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import Actividades
from Room.serializers import ActividadesSerializer

class InsertarActividad(APIView):

    def post(self, request):
        datoGuardar = ActividadesSerializer(data=request.data)
        if datoGuardar.is_valid():
            datoGuardar.save()
            return Response(datoGuardar.data, status=status.HTTP_201_CREATED)
        return Response(datoGuardar.errors, status=status.HTTP_400_BAD_REQUE)

    def get(self, request):
        dato = Actividades.objects.all()
        serializer = ActividadesSerializer(dato, many=True)
        return Response(serializer.data)

class EditarActividad(APIView):

    def get_object(self, pk):
        try:
            return Actividades.objects.get(pk=pk)
        except Actividades.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dato = self.get_object(pk)
        serializer = ActividadesSerializer(dato)
        return Response(serializer.data)

    def put(self, request, pk):
        dato = self.get_object(pk)
        valorAGuardar = ActividadesSerializer(dato, data=request.data)
        if valorAGuardar.is_valid():
            valorAGuardar.save()
            return Response(valorAGuardar.data, status=status.HTTP_200_OK)
        return Response(valorAGuardar.errors, status=status.HTTP_400_BAD_REQUEST)