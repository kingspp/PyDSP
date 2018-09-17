


def arr_conv(xn):
    xn=(xn.split(" "))
    xn=list(map(int,xn))
    return xn

def arr_convf(xn):
    xn=(xn.split(" "))
    xn=list(map(float,xn))
    return xn

def arr_convc(xn):
    xn=(xn.split(" "))
    xn=list(map(complex,xn))
    return xn


def pad_zero(r,xlen,hlen,h,x):
    if r!=0:
        if xlen > hlen:
            for i in range (hlen,xlen):
                h[i]=0
            hlen=xlen
        else:
            for j in range (xlen,hlen):
                x[j]=0
            xlen=hlen

def cir_conv(x,h,lmax,res,temp,h_rev):
    for i in range (lmax):
        res[0]+=x[i]*h_rev[i]

    for k in range (1,lmax):
        res[k]=0
        for j in range(1,lmax):
            temp[j]=h_rev[j-1]
        temp[0]=h_rev[lmax-1]
        for i in range(lmax):
            h_rev[i]=temp[i]
            res[k]+=x[i]*temp[i]