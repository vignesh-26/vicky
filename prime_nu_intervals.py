n,l=map(int,input().split())
i=n+1
while(i<l):
  s=0
  for k in range(2,i):
    if(i%k==0):
      s=1
      break
    k+=1
  if(s==0):
    print(i,end=" ")
  i+=1
  
