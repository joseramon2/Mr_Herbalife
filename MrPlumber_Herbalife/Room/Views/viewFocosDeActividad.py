from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Room.models import FocosDeActividad
from Room.serializers import FocosDeActividadSerializer

class focoActividad(APIView):

    def post(self, request):
        dato = FocosDeActividadSerializer(data=request.data)
        if dato.is_valid():
            dato.save()
            return Response(dato.data, status=status.HTTP_201_CREATED)
        return Response(dato.error, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        dato = FocosDeActividad.objects.all()
        serializer=FocosDeActividadSerializer(dato, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class focoActividadInfo(APIView):
    def get_object(self, pk):
        try:
            return FocosDeActividad.objects.get(pk=pk)
        except FocosDeActividad.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dato = self.get_object(pk)
        serializer = FocosDeActividadSerializer(dato)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        dato=self.get_object(pk)
        print(request.data)
        serializer = FocosDeActividadSerializer(dato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dato=self.get_object(pk)
        dato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)