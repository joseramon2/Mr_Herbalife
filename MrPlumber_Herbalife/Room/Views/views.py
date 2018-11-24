from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import Pisos
from Room.serializers import PisosSerializer

class PisosList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        lista_pisos = Pisos.objects.all()
        print(lista_pisos)
        serializer = PisosSerializer(lista_pisos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        valorAGuardar = PisosSerializer(data=request.data)
        if valorAGuardar.is_valid():
            try:
                valorAGuardar.save()
                return Response(valorAGuardar.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(("{confirmar:"+str([e])+"}"), status=status.HTTP_400_BAD_REQUEST)


class PisoNumero(APIView):

    def get_object(self, pk):
        try:
            return Pisos.objects.get(pk=pk)
        except Pisos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        detalle = self.get_object(pk)
        serializer = PisosSerializer(detalle)
        print(serializer.data)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        detalle = self.get_object(pk)
        valorAGuardar = PisosSerializer(detalle, data=request.data)
        if valorAGuardar.is_valid():
            valorAGuardar.save()
            return Response(valorAGuardar.data, status=status.HTTP_200_OK)
        return Response(valorAGuardar.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        detalle = self.get_object(pk)
        serializer = PisosSerializer(detalle)
        detalle.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)