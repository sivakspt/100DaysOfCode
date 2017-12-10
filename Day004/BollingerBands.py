import sys
sys.path.insert(0,'../Day002/')
import numpy as np
from EMA import EMA

def std_period(price,period):
    std=list(np.zeros(period-1))
    for i in range(period-1,len(price)):
        std.append(np.std(price[i-period+1:i+1]))
    return std

def BB(price,period=20,std_factor=2):
    middle_band=EMA(price,period)
    std=std_period(middle_band,period)
    upper_band=[x+2*y for (x,y) in zip(middle_band,std)]
    lower_band=[x-2*y for (x,y) in zip(middle_band,std)]
    return middle_band,upper_band,lower_band
