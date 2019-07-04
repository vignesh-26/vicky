n=int(input())
reverse=0
temp=n
while(n>0):
  c=n%10
  reverse=reverse*10+c
  n=n//10
if(temp==reverse):
  print("yes")
else:
  print("no")

