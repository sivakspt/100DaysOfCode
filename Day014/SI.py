def SI(openp,lowp,highp,closep,L=0.5):
    SI=[0]
    for i in range(1,len(closep)):
        h1=highp[i-1]
        l1=lowp[i-1]
        o1=openp[i-1]
        c1=closep[i-1]
        h2=highp[i]
        l2=lowp[i]
        o2=openp[i]
        c2=closep[i]
        K=max((h2-c1),(l2-c1))
        condition=max(abs(h2-c1),abs(l2-c1),abs(h2-l2))
        if condition == abs(h2-c1):
            R=(h2-c1)-.5*(l2-c1)+.25*(c1-o1)
        elif condition == abs(l2-c1):
            R=(l2-c1)-.5*(h2-c1)+.25*(c1-o1)
        else:
            R=(h2-l2)+.25*(c1-o1)
        num=(c2-c1)+.5*(c2-o2)+.25*(c1-o1)
        SI.append((50*num*K)/(R*L))
    return SI
