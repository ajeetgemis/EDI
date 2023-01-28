from django.contrib import admin
from .models import addmodel

# Register your models here.
@admin.register(addmodel)
class registeraddmodel(admin.ModelAdmin):
    list_display=['id','asnnumber','gsdb','supplier','date','pknumber']
  