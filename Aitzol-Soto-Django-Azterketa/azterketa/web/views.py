from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pertsona,Etxea,Alokairua
# Create your views here.
def index(request):
    pertsonak = Pertsona.objects.all
    etxeak = Etxea.objects.all
    alokairuak = Alokairua.objects.all
    return render(request,'index.html',{'pertsonak':pertsonak,'etxeak':etxeak,'alokairuak':alokairuak})

def addetxea(request):
    return render(request,'addEtxea.html')

def etxeagehitu(request):
    iz = request.POST['izena']
    he = request.POST['herria']
    kop = request.POST['pertsona_kop']
    etxe_berria = Etxea(izena=iz,herria=he,pertsona_kop=kop)
    etxe_berria.save()
    return HttpResponseRedirect(reverse('index'))

def updateetxea(request,etxea_id):
    etxea = Etxea.objects.get(id=etxea_id)
    return render(request,'updateEtxea.html',{'etxea':etxea})

def aldatuetxea(request,etxea_id):
    iz = request.POST['izena']
    he = request.POST['herria']
    kop = request.POST['pertsona_kop']
    etxea = Etxea.objects.get(id=etxea_id)
    etxea.izena = iz
    etxea.herria = he
    etxea.pertsona_kop = kop
    etxea.save()
    return HttpResponseRedirect(reverse('index'))

def deleteetxea(request,etxea_id):
    etxea = Etxea.objects.get(id=etxea_id)
    etxea.delete()
    return HttpResponseRedirect(reverse('index'))

def addpertsona(request):
    return render(request,'addPertsona.html')

def pertsonagehitu(request):
    iz = request.POST['izena']
    em = request.POST['emaila']
    nan = request.POST['nan']
    per_berria = Pertsona(izena=iz,emaila=em,nan=nan)
    per_berria.save()
    return HttpResponseRedirect(reverse('index'))

def updatepertsona(request,pertsona_id):
    pertsona = Pertsona.objects.get(id=pertsona_id)
    return render(request,'updatePertsona.html',{'pertsona':pertsona})

def aldatupertsona(request,pertsona_id):
    iz = request.POST['izena']
    em = request.POST['emaila']
    nan = request.POST['nan']
    pertsona = Pertsona.objects.get(id=pertsona_id)
    pertsona.izena =iz
    pertsona.emaila = em
    pertsona.nan = nan
    pertsona.save()
    return HttpResponseRedirect(reverse('index'))

def deletepertsona(request,pertsona_id):
    pertsona = Pertsona.objects.get(id=pertsona_id)
    pertsona.delete()
    return HttpResponseRedirect(reverse('index'))

def alokatu(request):
    pertsonak = Pertsona.objects.all
    etxeak = Etxea.objects.all
    return render(request,'alokatu.html',{'pertsonak':pertsonak,'etxeak':etxeak})

def alokatuetxea(request):
    et = request.POST['etxea']
    per = request.POST['pertsona']
    has_data = request.POST['alokatze_hasiera']
    am_data = request.POST['alokatze_amaiera']

    etxea = Etxea.objects.get(izena=et)
    pertsona = Pertsona.objects.get(izena=per)
    alokairua = Alokairua(etxea=etxea,pertsona=pertsona,alokatze_hasiera=has_data,alokatze_amaiera=am_data)
    alokairua.save()
    return HttpResponseRedirect(reverse('index'))