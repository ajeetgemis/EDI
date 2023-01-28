from django.shortcuts import render
from rest_framework import viewsets
from operation.models import  addmodel
from .serializer import asnserial
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

# Create your views here.
class asnapi(viewsets.ModelViewSet):
    queryset=addmodel.objects.all()
    serializer_class=asnserial
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]
  
    
   # return render(request,'base.html',{'values':'ajeet'})