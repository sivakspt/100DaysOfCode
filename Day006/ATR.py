import sys
sys.path.insert(0,'../Day001/')
import numpy as np
from SMA import SMA

def ATR(close,high,low,period=14):
    tr=[high[0]-low[0]]
    for i in range(1,len(close)):
        tr.append(max(high[i]-low[i],abs(high[i]-close[i-1]),abs(close[i-1]-low[i])))
    atr=SMA(tr[0:period],period)
    for i in range(period,len(tr)):
        atr.append((atr[i-1]*(period-1)+tr[i])/period)
    return atr

