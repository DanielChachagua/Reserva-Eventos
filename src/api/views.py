from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from servicios.models import *
from .serializers import *
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(http_method_names=['GET'])
def lista_servicios(request):
    servicios=Servicio.objects.all()
    serializer=ServicioSerializer(instance=servicios,many=True)
    repuesta={
        'Mensaje':'Lista de Servicios',
        'Datos':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def datos_servicio(request,id:int):
    servicios=get_object_or_404(Servicio,id=id)
    serializer=ServicioSerializer(instance=servicios)
    repuesta={
        'Datos Servicos':serializer.data
    }
    return Response(data=repuesta,status=status.HTTP_200_OK)