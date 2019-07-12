n=int(input())
k=list(map(int,input().split()))
c=0
for i in k:
  if(k.count(i)>=0):
    c=c+i
print(c)

