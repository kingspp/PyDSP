# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from uforms import Output
from uforms import Ndft_form
from uforms import Imp_form
from django.template import RequestContext
from django.core.urlresolvers import reverse
import numpy as np
from dsp import arr_conv
from dsp import arr_convf
from dsp import pad_zero
from dsp import cir_conv

res=np.zeros(10,dtype=int)
temp=np.zeros(10,dtype=int)





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
            result = str(np.convolve(x, h))
            output = "The Linear Convolution of x(n) and y(n) is: " + result
        return render_to_response('dsp/linear_conv.html', {'form':form, 'input1': xd, 'input2': hd, 'output':output,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Output()
        return render_to_response('dsp/linear_conv.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))

def imp_respf(request):
    if request.method == 'POST':
        form = Imp_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input1 = cd['input1']
            input2 = cd['input2']
            x=arr_convf(input1)
            y=arr_convf(input2)
            xd="x(n) = " + str(x)
            yd="y(n) = " + str(y)
            x=np.asarray(x)
            y=np.asarray(y)
            ORDER=1
            LEN=6
            h=np.zeros(LEN)
            sum=0.0

            for i in xrange(LEN):
                sum=0.0
                for k in xrange(1,ORDER+1):
                    if i-k >=0:
                        sum+=(y[k]*h[i-k])
                if i<=ORDER:
                    h[i]=x[i]-sum
                else:
                    h[i]=-sum

            output = "The First Order Impulse Responce h(n) is: " + str(h)
        return render_to_response('dsp/imp_respf.html', {'form':form, 'input1': xd, 'input2': yd, 'output':output,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Imp_form()
        return render_to_response('dsp/imp_respf.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))

def imp_resps(request):
    if request.method == 'POST':
        form = Imp_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input1 = cd['input1']
            input2 = cd['input2']
            x=arr_convf(input1)
            y=arr_convf(input2)
            xd="x(n) = " + str(x)
            yd="y(n) = " + str(y)
            x=np.asarray(x)
            y=np.asarray(y)
            ORDER=2
            LEN=6
            h=np.zeros(LEN)
            sum=0.0

            for i in xrange(LEN):
                sum=0.0
                for k in xrange(1,ORDER+1):
                    if i-k >=0:
                        sum+=(y[k]*h[i-k])
                if i<=ORDER:
                    h[i]=x[i]-sum
                else:
                    h[i]=-sum

            output = "The Second Order Impulse Responce h(n) is: " + str(h)
        return render_to_response('dsp/imp_respf.html', {'form':form, 'input1': xd, 'input2': yd, 'output':output,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Imp_form()
        return render_to_response('dsp/imp_respf.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))


def circular_conv(request):
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
            x = np.asarray(x)
            h = np.asarray(h)


            xlen=len(x)
            hlen=len(h)
            r=xlen-hlen

            if xlen>hlen:
                h=np.resize(h, xlen)
                lmax=xlen

            if hlen>xlen:
                x=np.resize(x, hlen)
                lmax=hlen

            if hlen==xlen:
                lmax=xlen

            pad_zero(r,xlen,hlen,h,x)
            h_rev=h[::-1]
            resn=np.resize(res, lmax)

            cir_conv(x,h,lmax,resn,temp,h_rev)

            res_rev='The Circular Convolution of x(n) and y(n) is: ' + str(resn[::-1])



        return render_to_response('dsp/circular_conv.html', {'form':form, 'input1': xd, 'input2':hd, 'output':res_rev,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Output()
        return render_to_response('dsp/circular_conv.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))

def ndft(request):
    if request.method == 'POST':
        form = Ndft_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input1 = cd['input1']
            x=arr_conv(input1)
            output = np.fft.fftn(x)
            output = 'The N-Point Discrete Fourier Transform of x(n) is : ' + str(output)
            indisp='Input Sequence x(n): ' + '[' + str(input1) + ']'
        return render_to_response('dsp/ndft.html', {'form':form, 'input1': indisp, 'output':output,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Ndft_form()
        return render_to_response('dsp/ndft.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))



