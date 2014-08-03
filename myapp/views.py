# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from uforms import Output
from django.template import RequestContext
from django.core.urlresolvers import reverse
import numpy

def arr_conv(xn):
    xn=(xn.split(" "))
    xn=map(int,xn)
    return xn


def home(request):
    return render(request, 'home.html', {'right_now':datetime.now()})

def contact(request):
    return render(request, 'home_contact.html',{'right_now':datetime.now()})

def about(request):
    return render(request, 'home_about.html',{'right_now':datetime.now()})

def linear_conv(request):
    if request.method == 'POST':
        form = Output(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input1 = cd['input1']
            input2 = cd['input2']
            x=arr_conv(input1)
            h=arr_conv(input2)
            xd="x(n) = " + str(x)
            hd="h(n) = " + str(h)
            result = str(numpy.convolve(x, h))
            output = "The Linear Convolution of x(n) and y(n) is: " + result
        return render_to_response('dsp/linear_conv.html', {'form':form, 'input1': xd, 'input2': hd, 'output':output,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Output()
        return render_to_response('dsp/linear_conv.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))

def imp_respf(request):
    return render(request, 'dsp/imp_respf.html',{'right_now':datetime.now()})

def imp_resps(request):
    return render(request, 'dsp/imp_resps.html',{'right_now':datetime.now()})

def circular_conv(request):
    return render(request, 'dsp/circular_conv.html',{'right_now':datetime.now()})

def ndft(request):
        return render(request, 'dsp/ndft.html',{'right_now':datetime.now()})


