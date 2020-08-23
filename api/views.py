from rest_framework import status
from .models import Viagem
from .serializers import ViagemSerializer
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response


class UpdateTravelVIEW(UpdateAPIView):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

    def patch(self, request, pk, format=None):
        """
        Partially Update Travel Objects
        Parameters:
            request: Request from DRF
            pk: Travel id
        """
        travel = Viagem.objects.get(id=pk)
        serializer = ViagemSerializer(
            travel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        """
        Update Travel Objects
        Parameters:
            request: Request from DRF
            pk: Id Travel
        """
        travel = Viagem.objects.get(id=pk)
        serializer = ViagemSerializer(
            travel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TravelVIEW(ListAPIView):

    def get(self, request: 'Request', format=None) -> Response:
        """
        List all travels objects for the current user
        Parameters:
            request: Request from client
        """
        travels = Viagem.objects.filter(user=request.user).all().order_by('-id')
        serializer = ViagemSerializer(travels, many=True)
        return Response(serializer.data)
