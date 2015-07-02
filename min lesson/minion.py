def stringcheck(a,b):
    if len(a)>len(b):
        a=a[0:len(a)]
        l=len(b)
    else :
        b=b[0:len(b)]
        l=len(a)
    s=''  
    p=''
    for i in range(0,l):
        if a[i]==b[i]:
            p=p+a[i]
        else:
            s=s+a[i]+b[i]
            break
        i=i+1
    return(p,s)
#x='yz'
#v='yx'
#
#print stringcheck(x,v)   
    


plow=[]   
def listcheck(low):
    for i in range(0,len(low)):
        while i < (len(low)-1):
            p,s=stringcheck(low[i],low[i+1])
            plow.append([p,s])
            break
        i=i+1
    return (plow)
        
            

words = ["ba", "ab", "cb"]
print listcheck(words)

    