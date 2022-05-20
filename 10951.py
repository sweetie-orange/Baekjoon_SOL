while(True):
    try:
        A,B=input().split()
        A=int(A)
        B=int(B)
        if A>=10 or B>=10 or A<=0 or B<=0:
            break
        print(A+B)
    except EOFError:
        break
