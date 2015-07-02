def answer(words):
    words = map(lambda x:x.lower(),words)
    def stringcheck(str1 , str2):
        if len(str1)>len(str2):
            str1 = str1[0:len(str1)]
            length = len(str2)
        else:
            str2 = str2[0:len(str2)]
            length = len(str1)
        s=''
        p=''
        for i in range(0,length):
            if str1[i] == str2[i]:
                p=p+str1[i]
            else:
                s=s+str1[i]+str2[i]
                break
            i=i+1
        return (p,s)


    def listcheck(words):
        plow = []
        for i in range (0,len(words)):
            while i <(len(words)-1):
                p,s=stringcheck(words[i],words[i+1])
                plow.append([p,s])
                break
            i=i+1
        return (plow)

    listpa = []
    def grouped(words) :
        words = listcheck(words)
        if words[0][0] == '':
            listpa.append(words[0][1])
        else:
            listpa.append(words[0][0])
            listpa.append(words[0][1])
        for i in range (1,len(words)):
            listpa.append(words[i][1])
            i=i+1
        return listpa

    listpa = grouped(words)
    s=''
    for i in range(0,len(listpa)-1):
        ele1 = listpa[i]
        ele2 = listpa[i+1]
        tempcom = list(set(ele1).intersection(set(ele2)))
        com = tempcom[0]
        indcom = ele1.find(com)
        poscom = ele2.find(com)

        if indcom > poscom:
            s = ele1[0:indcom] + ele2[poscom : len(ele2)]
        else:
            s = ele2[0:poscom] + ele1 [indcom : len(ele1)]
    return (s)



#words = ["sange","sangv","vol"]
#words = ["z", "yx", "yz"]
#words = ["y", "z", "xy"]
words = ["ba", "ab", "cb"]
#print listcheck(words)
print answer(words)
