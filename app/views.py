from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response


class ProductCrud(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PD=ProductSerializer(PQS,many=True)
        return Response(PD.data)
    def post(self,request):
        PSD=ProductSerializer(data=request.data)
        if PSD.is_valid():
            PSD.save()

            return Response({'message':'product is created'})
        return Response({'Failed':'Product is not created'})
    def put(self,request):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':"product is updated"})
        return Response({'Failed':"product data is not updated"})
    
