def answer(minions):       
    summ = 0
    if len(minions) <2:
        summ = summ+1
    else:
        None
    if len(minions) > 50:
        summ = summ+1
    else:
        None
    flat = [x for sublist in minions for x in sublist]
    maxx = max(flat)
    if maxx > 1024:
        summ = summ+1
    else:
        None
    for i in xrange(0,len(minions)):
        if minions[i][1]>= minions[i][2]:
            summ = summ+1
        else:
            None
    print summ
    if summ > 0:
        p = None
    else:
        timelist = []
        outp=[]
        for i in xrange (0,len(minions)):
            timelist.append(minions[i][0])
            totaltime = sum(timelist)
            comparelist = []
        for i in xrange (0,len(minions)):
            value = (((minions[i][1])/float(minions[i][2]))*minions[i][0]) + (1-(((minions[i][1])/float(minions[i][2]))))*totaltime
            comparelist.append([value,minions[i][0],i])
        scomparelist = sorted(comparelist, key =lambda x:(x[0],x[1]))
        for i in xrange(0,len(scomparelist)):
            outp.append(scomparelist[i][2])
        return outp

