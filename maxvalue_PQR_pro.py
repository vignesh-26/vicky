a,b,c,d=map(int,input().split())
t=list(map(int,input().split()))
v=[]
for i in range(0,len(t)):
  for j in range(i,len(t)):
    for k in range(j,len(t)):
      v.append(b*t[i]+c*t[j]+d*t[k])
print(max(v))
