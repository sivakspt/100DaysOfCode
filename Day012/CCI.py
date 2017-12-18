import sys
sys.path.insert(0,'../Day001/')
from SMA import SMA
from numpy import mean, absolute
import numpy as np

def mad(data, axis=None):
    return mean(absolute(data - mean(data, axis)), axis)

def CCI(close,high,low,period=20):
    tp=[(i+j+k)/3 for (i,j,k) in zip(close,high,low)]
    sma=SMA(tp,period)
    md=list(np.zeros(period-1))
    for i in range(period-1,len(tp)):
        md.append(mad(np.array(tp[i-period+1:i])))
    cci=[(i-j)/(.015*k) for (i,j,k) in zip(tp,sma,md)]
    return cci

