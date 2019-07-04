n=int(input())
k=list(map(int,input().split()))
k.sort()
a=[]
for i in range (len(k)-1):
  if k[i]==k[i+1]:
    a.append(k[i])
if a:
    for x in set(a):
        print(x,end=" ")
else:
    print("unique")

