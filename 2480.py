A,B,C=input().split()
A=int(A)
B=int(B)
C=int(C)
if A==B:
    if B==C:
        print(10000+A*1000)
    else:
        print(1000+A*100)
elif A==C:
    print(1000+A*100)
else:
    if B==C:
        print(1000+B*100)
    else:
        if A>B:
            if A>C:
                print(A*100)
            else:
                print(C*100)
        else:
            if B>C:
                print(B*100)
            else:
                print(C*100)
