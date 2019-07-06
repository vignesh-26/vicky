from itertools import permutations
n=input()
m=permutations(n)
for i in list(m):
    print("".join(i))
