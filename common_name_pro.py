
n=int(input())
k=[]
for i in range(0,n):
  l=input()
  k.append(l)
m=[]
for i in zip(*k):
  if(i.count(i[0])==len(i)):
    m.append(i[0])
  else:
    break
print(''.join(m))
