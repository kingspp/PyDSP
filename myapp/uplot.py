from pylab import *


def gp(res,num,c):
    t = arange(0,num,1)
    s = res

    xlabel('Time ')
    ylabel('Magnitude')

    if c=='l':
        title('Linear Convolution')
    elif c== 'c':
        title('Circular Convolution')
    elif c== 'if':
        title('Impulse Responce [First Order]')
    elif c== 'is':
        title('Impulse Responce [Second Order]')
    elif c== 'ac':
        n=int(num/2)
        t=arange(-n,n+1,1)
        xlabel('Amplitude')
        title('Autocorrelation')

    elif c== 'cc':
        n=int(num/2)
        t=arange(-n,n+1,1)
        xlabel('Amplitude')
        title('Crosscorrelation')


    stem(t, s)
    grid(True)
    savefig("Vote/media/plots/test.png")
