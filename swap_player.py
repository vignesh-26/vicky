st=list(input())
i=0
while(i<len(st)):
  temp=st[i]
  st[i]=st[i+1]
  st[i+1]=temp
  i+=2
print("".join(st))
