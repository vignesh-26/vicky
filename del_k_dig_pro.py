from itertools import combinations
n,m=list(input().split())
k=[]
m=int(m)
l=combinations(n,len(n)-m)
for i in l:
  k.append("".join(i))
print(min(k))

