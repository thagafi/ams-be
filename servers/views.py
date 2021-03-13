from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.views import APIView
from users.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import ServersModel
from .serializers import ServerSerializer
from config.pagination import CustomPagination
from rest_framework.response import Response
from django.http import HttpResponse
import csv

class ServerGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    permission_object = 'users'
    queryset = ServersModel.objects.all()
    serializer_class = ServerSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk).data
            })

        return self.list(request)

    def post(self, request):
        return Response({
            'data': self.create(request).data
        })

    def put(self, request, pk=None):

        return Response({
            'data': self.partial_update(request, pk).data
        })

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class ExportServerAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=servers.csv'

        servers = ServersModel.objects.all()
        writer = csv.writer(response)

        writer.writerow([
                            'ID',
                            'Server Name',
                            'Location',
                            'Status',
                            'Network',
                            'CPU',
                            'RAM',
                            'Size of Monitor',
                            'Operating System',
                            'Brand',
                            'Date',
                            'User'
                        ])

        for server in servers:
            writer.writerow([
                                server.id,
                                server.server_name,
                                server.location,
                                server.status,
                                server.network,
                                server.cpu,
                                server.ram,
                                server.monitor_size,
                                server.os,
                                server.brand,
                                server.date,
                                server.user.username
                            ])
            
        return response