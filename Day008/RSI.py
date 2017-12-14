def RSI(close,period):
    RSI=[]
    RS=0
    for i  in range(1,len(close)-period):
        avggain=0
        avgloss=0
        for j in range(period):
            if close[i+j]>=close[i+j-1]:
                avggain+=close[i+j]-close[i+j-1]
            else:
                avgloss+=close[i+j-1]-close[i+j]
        if avgloss>0:
            RS=avggain/avgloss
        else:
            RSI.append(100)
        RSI.append(100-100/(1+RS))
    return RSI




