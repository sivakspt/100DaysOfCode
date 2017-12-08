import sys
sys.path.insert(0,'../Day001/')
import numpy as np
import SMA

def EMA(price,period):
    ema=SMA.SMA(price[0:period],period)
    multiplier=2/(period+1)
    for i in range(period,len(price)):
        ema.append((price[i]-ema[i-1])*multiplier+ema[i-1])
    return ema
