from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from AppADANGELOCoder19.models import Familiar

# Create your views here.
def verFamiliares(request):

    familiares = Familiar.objects.all()

    template = loader.get_template('familiares.html')
    
    documento = template.render({'familiares': familiares})
    return HttpResponse(documento)