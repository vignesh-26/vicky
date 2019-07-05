kk=int(input())
l=[]
for i in range(0,kk):
    m=list(map(int,input().split()))
    for i in (m):
      l.append(i)
    l.sort()
print(*l,end="")
