from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from sistema_fcc_api.serializers import *
from sistema_fcc_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json
class MateriasAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        materias = Materias.objects.filter().order_by("id") #NO SE AGREGA NADA EN EL () DE FILTER PORQUE NO ES POR USUARIOS, SOLO SE FILTRA POR ID Y YA
        materias["materias_dia"]= json.loads(materias["materias_dia"])
        lista = MateriaSerializer(materias, many=True).data

        return Response(lista, 200)

class MateriasView(generics.CreateAPIView):

    #Obtener usuario por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):#estructura general de la funcion
        materia = get_object_or_404(Materias, id = request.GET.get("id"))
        materia = MateriaSerializer(materia, many=False).data #SE DECLARA ASI PARA EVITAR PROBLEMAS CON NOMBRE COMO "materia" o "materias" ERROR MIO POR PARTE DE ESCOGER NOMBRE VARIABLES JSON Y FUNCIONES
        return Response(materia, 200)
    @transaction.atomic
    def post(self, request, *args, **kwargs):#estructura basica
        
        materia = MateriaSerializer(data=request.data)# el serializer va en el serializer de pyi o el extension
        if materia.is_valid():
            
          
            materia = Materias.objects.create(  nrc=request.data["nrc"],
                                                name=request.data["name"],
                                                seccion=request.data["seccion"],
                                                materias_dia = json.dumps(request.data["materias_dia"]),
                                                horario_inicio=request.data["horario_inicio"],
                                                horario_final=request.data["horario_final"],
                                                salon=request.data["salon"],
                                                programa=request.data["programa"])
            materia.save()
            return Response({"materia_created_id": materia.id}, 201)
    
        return Response(materia.errors ,status=status.HTTP_400_BAD_REQUEST)
    
#Se tiene que modificar la parte de edicion y eliminar
class MateriasViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        materia = get_object_or_404(Maestros, id=request.data["id"])
        materia.nrc = request.data["nrc"]
        materia.name = request.data["name"]
        materia.seccion = request.data["seccion"]
        materia.materia_dia = json.dumps(request.data["materia_dia"])
        materia.horario_inicio = request.data["horario_inicio"]
        materia.horario_final = request.data["horario_final"]
        materia.salon = request.data["salon"]
        materia.programa = request.data["programa"]
        materia.save()
        materia = MateriaSerializer(materia, many=False).data

        return Response(materia,200)
    
    
    def delete(serlf, request, *args, **kwargs):
        profile= get_object_or_404(Materias, id=request.GET.get("id"))
        try:
            profile.delete()
            return Response({"details": "Materia eliminada"})
        except Exception as e:
            return Response({"details": "Algo pasó al eliminar"})