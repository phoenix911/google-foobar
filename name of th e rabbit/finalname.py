def answer(names):
    names = map(lambda x:x.lower(),names)
    import string
    keya = list(string.ascii_lowercase)
    keyn = range(1,27)
    aton = dict()
    for keyi in range (0,26):
        aton.update({keya[keyi]:keyn[keyi]})
    def a2n(nam):
        nam = list(nam)
        sum=0
        for i in range(0,(len(nam))):
            sum = sum + aton[nam[i]]
            i=i+1
        return sum
    arrayofnum = []
    namearr = []
    for i in range(0,len(names)):
        arrayofnum.append ([a2n(names[i]),names[i]])
        i=i+1
        saon = sorted(arrayofnum, reverse = True)
    for j in range (0,len(saon)):
        namearr.append(saon[j][1])
        j=j+1
    return (namearr)
    
    
names = ['SANGE' , 'VERMA']  
print answer(names)
        
    