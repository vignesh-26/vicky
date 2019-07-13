cv=int(input())
while cv%10==0:
  cv=cv//10
cv=str(cv)
z=cv[::-1]
if cv==z:
  print("yes")
else:
    print("no")
