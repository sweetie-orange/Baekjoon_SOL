Test=int(input())
for i in range(Test):
    A=[int(x) for x in input().split()]
    average=sum(A[1:])/A[0]
    number=0
    for i in range(1,len(A)):
        if A[i]>average:
            number+=1
    real=number/A[0]*100
    print(f'{real :.3f}'+"%")
