
n=int(input())
k=list(map(int,input().split()))
flag=0
for i in k:
  if (k.count(i)>1):
      print(i)
      flag=1
      break
if(flag==0):
      print("unique")
