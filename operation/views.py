from django.shortcuts import render,HttpResponseRedirect
from .forms import formaddmodel
from .models import addmodel
from django.views.decorators.cache import cache_page

# Create your views here.
global queryset
def test(request):
    
    queryset=addmodel.objects.all()
    return render(request,'templatetest.html',{'retrivevalue':queryset})

def editone(request,id):
    if request.method=='POST':
        queryset=addmodel.objects.get(pk=id)
        fm=formaddmodel(request.POST,instance=queryset)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/') 
           # return render(request,'add.html')
    else:
        queryset=addmodel.objects.get(pk=id)
        #print(type(queryset))
        fm=formaddmodel(instance=queryset)
        
           
        print(type(fm))

        return render(request,'edit.html',{'objdict':fm})

       
def delete(request,id):
    if request.method=='POST':
        objmod=addmodel.objects.get(pk=id)

        print(objmod)
        objmod.delete()
        return HttpResponseRedirect('/')

def success(request):
    return render(request,'success.html',{'success':'Form Submited'})
#global queryset

@cache_page(60) 
def addrecord(request):
    global queryset
    if request.method=='POST':

        nm=formaddmodel(request.POST)  
        if nm.is_valid():
         print(nm.cleaned_data['asnnumber'])
         print(nm.cleaned_data['date'])
         asn=nm.cleaned_data['asnnumber']
         gs=nm.cleaned_data['gsdb']
         sup=nm.cleaned_data['supplier']
         dat=nm.cleaned_data['date']
         pkn=nm.cleaned_data['pknumber']
         adddatabase=addmodel(asnnumber=asn,gsdb=gs,supplier=sup,date=dat,pknumber=pkn)
         adddatabase.save()
         queryset=addmodel.objects.all()
         nm=formaddmodel()
         return render(request,'add.html',{'value':nm,'retrivevalue':queryset})
         
         #return render(request,'add.html',retrivevalue)
         #return HttpResponseRedirect('/success/')
    else:
        
        #retrivevalue={'modelvalue':queryset}
        nm=formaddmodel()
        
        queryset=addmodel.objects.all()
        return render(request,'add.html',{'value':nm,'retrivevalue':queryset})
        

    return render(request,'add.html',{'value':nm,'retrivevalue':queryset})
