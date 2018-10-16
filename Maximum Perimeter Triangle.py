from itertools import *
n=int(input())
strr=input()
ans=[]
ans1=[]
ans0=[]
c=0
true=0
li=strr.split()
for i in range(len(li)):
    li[i]=int(li[i])
ans=list(permutations(li,3))
for i in range(len(ans)):
    l=list(ans[i])
    l.sort()
    count=0
    if((l[0]+l[1])>l[2]):
        count=l[0]+l[1]+l[2]
        ans0.append(count)
        ans1.append(i)
        true=1
if(true!=1):
    print("-1")
else:
    pos=0
    large=0
    for i in range(len(ans0)):
        if(ans0[i]>large):
            large=ans0[i]
            pos=i
    for i in range(len(ans1)):
        if(i==pos):
            for j in range(len(ans)):
                if(j==ans1[pos]):
                    s=list(ans[j])
                    s.sort()
                    for i in range(len(s)):
                        print(s[i],end=" ")

