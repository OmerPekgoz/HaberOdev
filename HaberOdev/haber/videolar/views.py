from django.shortcuts import render,get_object_or_404
from .models import Haberler,Ekonomi,Gündem
# Create your views here.
def home(request):
    haber=Haberler.objects.all()
    ekonomi=Ekonomi.objects.all()
    gün=Gündem.objects.all()
    return render(request,'index.html',{'haber':haber,'ekonomi':ekonomi,'gündem':Gündem})

def sonhaberdetay(request,sonhaber_id):
    sonhaber=get_object_or_404(Haberler,pk=sonhaber_id)
    return render(request,'haber.html',{'sonhaber':sonhaber})

def gündemdetay(request,gün_id):
    gün=get_object_or_404(Gündem,pk=gün_id)
    return render(request,'gündem.html',{'gundem':gün})





