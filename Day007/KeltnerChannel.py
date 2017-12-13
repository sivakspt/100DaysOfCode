import sys
sys.path.insert(0,'../Day002/')
sys.path.insert(0,'../Day006/')
import numpy as np
from EMA import EMA
from ATR import ATR

def KeltnerChannel(close,high,low,ema_period=20,atr_period=10,shift=2):
    middle_line=EMA(close,ema_period)
    atr=ATR(close,high,low,atr_period)
    upper_line=[i+shift*j for (i,j) in zip(middle_line,atr)]
    lower_line=[i-shift*j for (i,j) in zip(middle_line,atr)]
    return middle_line,upper_line,lower_line
