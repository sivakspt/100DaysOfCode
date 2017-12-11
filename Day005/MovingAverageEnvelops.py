import sys
sys.path.insert(0,'../Day002/')
import numpy as np
from EMA import EMA

def Envelop(price,period=20,envelop_width=5):
    avg=EMA(price,period)
    upper_envelop=[x+x*envelop_width/100 for x in avg]
    lower_envelop=[x-x*envelop_width/100 for x in avg]
    return upper_envelop,lower_envelop
