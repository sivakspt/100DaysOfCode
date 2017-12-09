import sys
sys.path.insert(0,'../Day002/')
import numpy as np
from EMA import EMA

def MACD(price,fast_period=12,slow_period=26,signal_period=9):
    macd=[]
    fast=EMA(price,fast_period)
    slow=EMA(price,slow_period)
    macd=[x-y for (x,y) in zip(fast,slow)]
    signal=EMA(macd,signal_period)
    return macd,signal
