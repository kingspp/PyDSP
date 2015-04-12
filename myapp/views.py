# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from uforms import Output
from uforms import Ndft_form
from uforms import Imp_form
from uforms import Dft_idft
from uforms import Nyq
from django.template import RequestContext
from django.core.urlresolvers import reverse
from uplot import gp
from uplot import nyq_plot
from uplot import twoplot
from uplot import oneplot
import numpy as np
from dsp import arr_conv
from dsp import arr_convf
from dsp import arr_convc
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

def dft_idft(request):
    if request.method == 'POST':
        form = Dft_idft(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            input1 = cd['input1']
            choice = cd['choice']

            x=arr_convc(input1)
            x=np.asarray(x)
            if choice=='Yes':
                res=np.fft.fft(x)
                ch="Your choice was DFT"
                result="The DFT of x(n) is: " + str(res)
                ch=1
            elif choice=='No':
                res=np.fft.ifft(x)
                ch="Your choice was IDFT"
                result="The IDFT of x(n) is: " + str(res)
                ch=0
            xd="x(n) = " + str(x)
            #c='l'
            num=len(res)

            a=res.real
            b=res.imag

            num=len(res)
            numr=len(a)
            numi=len(b)

            for i in range (numi):
                if b[i]!=0j:
                    twoplot(numr,numi,a,b,ch)
                else:
                    oneplot(res,num,ch)


            #gp(res,num,c)
            graphy='<img class="img-responsive" src="http://kingspp.pythonanywhere.com/media/plots/test.png" ></img>'
        return render_to_response('dsp/dft_idft.html', {'form':form, 'input1': xd, 'choice': ch, 'output':result, 'graphy':graphy,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Dft_idft()
        return render_to_response('dsp/dft_idft.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))

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
            resultd=np.convolve(x, h)
            num=len(resultd)
            result = str(resultd)
            output = "The Linear Convolution of x(n) and y(n) is: " + result
            c='l'
            gp(resultd,num,c)
            graphy='<img src="http://kingspp.pythonanywhere.com/media/plots/test.png" height="400px" width="500px" ></img>'
        return render_to_response('dsp/linear_conv.html', {'form':form, 'input1': xd, 'input2': hd, 'output':output, 'graphy':graphy, 'right_now':datetime.now()}, context_instance=RequestContext(request))
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

            c='if'
            num=len(h)
            gp(h,num,c)
            graphy='<img src="http://kingspp.pythonanywhere.com/media/plots/test.png" height="400px" width="500px" ></img>'
            output = "The First Order Impulse Responce h(n) is: " + str(h)
        return render_to_response('dsp/imp_respf.html', {'form':form, 'input1': xd, 'input2': yd, 'output':output, 'graphy':graphy,'right_now':datetime.now()}, context_instance=RequestContext(request))
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
            c='is'
            num=len(h)
            gp(h,num,c)
            graphy='<img src="http://kingspp.pythonanywhere.com/media/plots/test.png" height="400px" width="500px" ></img>'
            output = "The Second Order Impulse Responce h(n) is: " + str(h)
        return render_to_response('dsp/imp_respf.html', {'form':form, 'input1': xd, 'input2': yd, 'output':output, 'graphy':graphy,'right_now':datetime.now()}, context_instance=RequestContext(request))
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
            resn=resn[::-1]
            num=len(resn)
            c='c'
            gp(resn,num,c)
            graphy='<img src="http://kingspp.pythonanywhere.com/media/plots/test.png" height="400px" width="500px" ></img>'
            res_rev='The Circular Convolution of x(n) and y(n) is: ' + str(resn)
        return render_to_response('dsp/circular_conv.html', {'form':form, 'input1': xd, 'input2':hd, 'output':res_rev, 'graphy':graphy,'right_now':datetime.now()}, context_instance=RequestContext(request))
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
            num=len(output)
            c='nd'
            gp(output,num,c)
            graphy='<img src="http://kingspp.pythonanywhere.com/media/plots/test.png" height="400px" width="500px" aligh="center"></img>'

            output = 'The N-Point Discrete Fourier Transform of x(n) is : ' + str(output)
            indisp='Input Sequence x(n): ' + '[' + str(input1) + ']'
        return render_to_response('dsp/ndft.html', {'form':form, 'input1': indisp, 'output':output, 'graphy':graphy,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Ndft_form()
        return render_to_response('dsp/ndft.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))

def auto_corr(request):
    if request.method == 'POST':
        form = Ndft_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input1 = cd['input1']
            x=arr_conv(input1)
            output=np.correlate(x,x,'full')
            output=np.asarray(output)
            c='ac'
            num=len(output)
            gp(output,num,c)
            graphy='<img src="http://kingspp.pythonanywhere.com/media/plots/test.png" height="400px" width="500px" ></img>'
            output = 'The Autocorrelation of x(n) is : ' + str(output)
            indisp='Input Sequence x(n): ' + '[' + str(input1) + ']'
        return render_to_response('dsp/auto_corr.html', {'form':form, 'input1': indisp, 'output':output, 'graphy':graphy, 'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Ndft_form()
        return render_to_response('dsp/auto_corr.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))

def cross_corr(request):
    if request.method == 'POST':
        form = Output(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input1 = cd['input1']
            input2 = cd['input2']
            x=arr_conv(input1)
            h=arr_conv(input2)
            output=np.correlate(x,h,'full')
            output=np.asarray(output)
            c='cc'
            num=len(output)
            gp(output,num,c)
            graphy='<img src="http://kingspp.pythonanywhere.com/media/plots/test.png" height="400px" width="500px" ></img>'
            output = 'The Crosscorrelation of x(n) and h(n) is : ' + str(output)
            indispx='Input Sequence x(n): ' + '[' + str(input1) + ']'
            indisph='Input Sequence h(n): ' + '[' + str(input2) + ']'
        return render_to_response('dsp/cross_corr.html', {'form':form, 'input1': indispx,'input2': indisph, 'output':output, 'graphy':graphy,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Output()
        return render_to_response('dsp/cross_corr.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))

def sampling(request):
    if request.method == 'POST':
        form = Nyq(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input1 = cd['input1']
            input2 = cd['input2']
            nyq_plot(input1,input2)
            graphy='<img src="http://kingspp.pythonanywhere.com/media/plots/test.png" height="400px" width="600px" ></img>'
        return render_to_response('dsp/sampling.html', {'form':form, 'graphy':graphy,'right_now':datetime.now()}, context_instance=RequestContext(request))
    else:
        form = Nyq()
        return render_to_response('dsp/sampling.html', {'form': form,'right_now':datetime.now()}, context_instance=RequestContext(request))




