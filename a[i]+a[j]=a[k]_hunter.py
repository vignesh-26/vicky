k=int(input())
a=(input().split())
for i in range(len(a)):
  for j in range(i+1,len(a)):
    for k in range(j+1,len(a)):
      if (int(a[i])+int(a[j])==int(a[k])):
        print(a[i],a[j],a[k])
