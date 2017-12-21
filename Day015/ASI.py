import sys
sys.path.insert(0,'../Day014/')
from SI import SI

def ASI(openp,lowp,highp,closep,L=0.5):
    ASI=[]
    si=SI(openp,lowp,highp,closep,L)
    ASI.append(si[0])
    for i in range(1,len(si)):
        ASI.append(ASI[-1]+si[i])
    return ASI
