from itertools import *
num =int(input())
c=0
while(c<num):
    true = 0
    c=c+1
    inp1=input()
    inp2=input()
    inp3=input()
    li=inp1.split()
    k=int(li[-1])
    a=inp2.split()
    b=inp3.split()
    for i in range(len(a)):
        a[i]=int(a[i])
    for i in range(len(b)):
        b[i]=int(b[i])
    per_a=list(permutations(a))
    per_b=list(permutations(b))
    for i in range(len(per_a)):
        aa=list(per_a[i])
        for j in range(len(per_b)):
            bb = list(per_b[j])
            count = 0
            for kk in range(int(li[0])):
                ans = (aa[kk] + bb[kk])
                if (ans >= k):
                    count = count + 1
                if (count == int(li[0])):
                    true = 1
    if (true == 0):
        print("NO")
    else:
        print("YES")





