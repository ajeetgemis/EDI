from rest_framework import serializers
from operation.models import addmodel

class asnserial(serializers.ModelSerializer):
    class Meta:
        model=addmodel
        fields=['asnnumber','gsdb','supplier','date','pknumber']