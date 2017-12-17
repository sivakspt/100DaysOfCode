import numpy as np

def MF(rmf,period):
    mfr=list(np.zeros(period))
    for i in range(period,len(rmf)):
        pmf=0
        nmf=0
        for j in range(1,period):
            if rmf[i-period+j]>rmf[i-period+j-1]:
                pmf+=rmf[i-period+j]
            else:
                nmf+=rmf[i-period+j]
        mfr.append(pmf/nmf)
    return mfr

def MFI(close,high,low,volume,period=14):
    typicalprice=[(i+j+k)/3 for (i,j,k) in zip(close,high,low)]
    rmf=[i*j for (i,j) in zip(typicalprice,volume)]
    mfr=MF(rmf,period)
    mfi=[100-100/(1+i) for i in mfr]
    return mfi


