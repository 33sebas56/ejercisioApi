import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

# Create your views here.
class SumaView(APIView):
    def get(self,request, * arg, ** kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        suma=int(num_uno)+ int(num_dos)
        return Response(suma, status=status.HTTP_200_OK)
class RestaView(APIView):
    def get(self,request, * arg, ** kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        rest=int(num_uno)- int(num_dos)
        return Response(rest, status=status.HTTP_200_OK)
class MultiplicacionView(APIView):
    def get(self,request, * arg, ** kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        multiplicacion=int(num_uno)* int(num_dos)
        return Response(multiplicacion, status=status.HTTP_200_OK)
class DivisionView(APIView):
    def get(self,request, * arg, ** kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        if int(num_dos)==0:
            return Response("syntax error", status=status.HTTP_400_BAD_REQUEST) 
        division=int(num_uno)/ int(num_dos)
        
        return Response(division, status=status.HTTP_200_OK)