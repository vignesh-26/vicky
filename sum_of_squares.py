n=int(input())
s=0
while(n!=0):
  i=n%10
  s=s+i**2
  n=n//10
print(s)
