Arr=list(map(int,input().split()))
S=0
for i in range(0,len(Arr)):
    S+=Arr[i]
print(S)
median=S/(len(Arr))
print(median)
