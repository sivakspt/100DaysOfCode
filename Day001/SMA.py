import numpy as np

def SMA(price,period):
    sma=[]
    sma+=list(np.zeros(period-1))
    for i in range(period-1,len(price)):
        sma.append(sum(price[i-period+1:i+1])/period)
    return sma
