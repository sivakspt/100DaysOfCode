import sys
sys.path.insert(0,'../Day002/')
from EMA import EMA

def CV(high,low,period=20,change_period=10):
    hl=[x-y for (x,y) in zip(high,low)]
    hlema=EMA(hl)
    CV=0
    for i in range(change_period-1):
        CV.append(0)
    for i in range(change_period,len(hl)):
        j=i-change_period
        CV.append((hl[i]-hl[j])*100/hl[j])
    return CV


