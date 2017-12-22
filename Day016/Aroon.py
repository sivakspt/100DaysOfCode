import numpy as np

def Aroon(close,period=14):
    Aroon_up=list(np.zeros(period-1))
    Aroon_down=list(np.zeros(period-1))
    for i in range(period-1,len(close)):
        l=close[i-period+1:i].index(min(close[i-period+1:i])) 
        h=close[i-period+1:i].index(max(close[i-period+1:i])) 
        Aroon_up.append((h+1)*100/25)
        Aroon_down.append((l+1)*100/25)
    return Aroon_up,Aroon_down
