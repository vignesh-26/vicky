n=int(input())
t=map(int,input().split())
k=[]
for i in t:
  e=bin(i)
  k.append(e)
f=sorted(k)
f.reverse()
for j in f:
  print(int(j,2))
