import string
arr = map(lambda x:x.lower(),arr)
a=list(string.ascii_lowercase)
b = range(1,27)
aton = dict()
for i in range(0,26):
    aton.update({a[i]:b[i]})
def nametonumber(nam):
    nam = list(nam)
    nam = list(nam)
    sum = 0
    for i in range(0,(len(nam))):
        sum = sum + aton[nam[i]]
        i = i+1
    return sum

arrayofnum = []
namearr = []
def answer(name):
    for i in range(0,len(name)):
        arrayofnum.append ([nametonumber(name[i]),name[i]])
        i=i+1
        saon = sorted(arrayofnum, reverse = True)
    for j in range (0,len(saon)):
        namearr.append(saon[j][1])
        j=j+1
    return(namearr)
    
arr = ['SANG','VERMA']
pola = map(lambda x:x.lower(),arr)
print pola
print type(arr)

an = answer(arr)
print an