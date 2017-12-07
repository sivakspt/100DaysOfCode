import numpy as np

def SMA(price,period):
    sma=[]
    sma+=list(np.zeros(period))
    for i in range(period,len(price)):
        sma.append(sum(price[i-period:i])/period)
    return sma
