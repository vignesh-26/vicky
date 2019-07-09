n=int(input())
k=list(map(int,input().split()))
for i in range(0,n):
  if(i%2==0 and k[i]%2==1):
    print(k[i],end=" ")
  if(i%2==1 and k[i]%2==0):
    print(k[i],end=" ")
