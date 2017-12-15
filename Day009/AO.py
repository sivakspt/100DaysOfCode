import sys
sys.path.insert(0,'../Day001/')
import numpy as np
from SMA import SMA

def AO(high,low):
    day_avgs=[(i+j)/2 for (i,j) in zip(high,low)]
    sma5=SMA(day_avgs,5)
    sma34=SMA(day_avgs,34)
    AO=[i-j for (i,j) in zip(sma5,sma34)]
    return AO
