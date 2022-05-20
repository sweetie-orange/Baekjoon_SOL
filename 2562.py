L=[]
for x in range(0,9):
    n=int(input())
    L.append(n)
maximum=max(L)
print(maximum)
for i in range(0,9):
    if L[i]==maximum:
        print(i+1)
