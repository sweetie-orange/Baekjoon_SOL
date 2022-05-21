N=int(input())
hansu=99
if N<100:
    print(N)
else:
    for i in range (100,N+1):
        AC=(int(i/100)+i%10)
        B2=2*int(i%100/10)
        if AC==B2:
            hansu=hansu+1
    print(hansu)
