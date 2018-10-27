num=int(input())
strr=input()
li=strr.split()
for i in range(len(li)):
    li[i]=int(li[i])
li.sort()
true=0
count=0
pos=0
while(true==0):
    temp=0
    small=4+li[pos]
    for i in range(pos,len(li)):
        if(li[i]<=small):
            pos=i+1
            temp=1
    if(temp==1):
        count=count+1
    if(pos==len(li)):
        true=1
print(count)

