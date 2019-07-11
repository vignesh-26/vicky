k,m=map(int,input().split())
c=[]
for i in range(k):
  p=set(map(int,input().split()))
  c.append(p)
n=p.intersection(*c)
print(*n)
