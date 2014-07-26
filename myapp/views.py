# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Queries





def home(request):
    return render(request, 'home.html', {'right_now':datetime.now()})

def contact(request):
    return render(request, 'home_contact.html',{'right_now':datetime.now()})



def linear_conv(request):
    return render(request, 'linear_conv.html',{'right_now':datetime.now()})

def imp_respf(request):
    return render(request, 'dsp/imp_respf.html',{'right_now':datetime.now()})

def imp_resps(request):
    return render(request, 'dsp/imp_resps.html',{'right_now':datetime.now()})

def circular_conv(request):
    return render(request, 'dsp/circular_conv.html',{'right_now':datetime.now()})

def ndft(request):
        return render(request, 'dsp/ndft.html',{'right_now':datetime.now()})




