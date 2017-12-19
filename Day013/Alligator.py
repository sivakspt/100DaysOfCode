import sys
sys.path.insert(0,'../Day001')
from SMA import SMA
import numpy as np

def offsetter(price,offset):
    offseted=list(np.zeros(offset))
    for i in price[:-offset]:
        offseted.append(i)
    return offseted

def Alligator(close):
    jawval=SMA(close,13)
    teethval=SMA(close,8)
    lipsval=SMA(close,5)
    jaw=offsetter(jawval,8)
    teeth=offsetter(teethval,5)
    lips=offsetter(lipsval,3)
    return jaw,teeth,lips
