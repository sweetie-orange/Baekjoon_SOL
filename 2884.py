H,M=input().split()
H=int(H)
M=int(M)
if H>0:
    if M<45:
        nM=M+60-45
        nH=H-1
        print(nH,nM)
    else:
        nM=M-45
        print(H,nM)
else:
    if M<45:
        nM=M+60-45
        nH=23
        print(nH,nM)
    else:
        nM=M-45
        print(H,nM)
