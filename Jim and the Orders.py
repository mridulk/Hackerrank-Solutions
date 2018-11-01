num=int(input())
matrix = []; columns = []
# initialize the number of rows
for i in range(0,num):
    matrix += [0]
# initialize the matrix
for i in range (0,num):
    matrix[i] = [0]*3
#print(matrix)
order=[]
pre=[]
for i in range(num):
    strr=input()
    li=strr.split()
    order.append(int(li[0]))
    pre.append(int(li[1]))
#print(order)
for i in range(num):
    matrix[i][0]=order[i]
for i in range(num):
    matrix[i][1]=pre[i]
#print(matrix)
sum=[]
t=0
for i in range(num):
    sum.append(order[i]+pre[i])
for i in range(num):
    matrix[i][2]=sum[i]
#print(matrix)
sum.sort()
#print(sum)
for i in range(num):
    tr=0
    if(t==1):
        tr=1
    t=0
    for j in range(num):
        if(tr==1):
            j=j+1
        if(j==(num-1)):
            print((j + 1), end=" ")
            break;
        else:
            if(sum[i]==matrix[j][2]):
                if(i==(num-1)):
                    print((j + 1), end=" ")
                    break;
                else:
                    if ((sum[i] != sum[i + 1])):
                        print((j + 1),end=" ")
                        break;
                    else:
                        print((j + 1), end=" ")
                        t=1
                        break;









