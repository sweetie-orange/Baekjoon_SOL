N=int(input())
A=[int(x) for x in input().split()]
maximum=max(A)
sumoftest=0
for i in A:
    sumoftest=sumoftest+i/maximum*100
newaverage=sumoftest/N
print(newaverage)
