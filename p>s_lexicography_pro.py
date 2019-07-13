bl=input()
for i in range(len(bl)):
  if(bl[i] < bl[i+1]):
    print(bl[i+1:])
    break
