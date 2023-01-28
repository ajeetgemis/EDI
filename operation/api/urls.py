from django.contrib import admin
from django.urls import path,include
from operation.api import  views
from rest_framework.routers import DefaultRouter




router=DefaultRouter()
router.register('asnapi',views.asnapi,basename='asnapi')
urlpatterns = [    
    path('',include(router.urls)),
   
]
