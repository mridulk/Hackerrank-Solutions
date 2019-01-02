n=int(input())
strr=input()
li=strr.split()
lii=list()
for i in li:
    lii.append(int(i))
'''print(lii)'''
for i in range(1,n):
    t=i
    while(lii[t-1]>lii[t]):
        temp=lii[t-1]
        lii[t-1]=lii[t]
        lii[t]=temp
        '''print(lii)'''
        if(t>1):
            t=t-1
        else:
            break
    print( " ".join(str(x) for x in lii))
