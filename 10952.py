A=1
B=1
while(True):
    A,B=input().split()
    A=int(A)
    B=int(B)
    if A==0&B==0:
        break
    print(A+B)
