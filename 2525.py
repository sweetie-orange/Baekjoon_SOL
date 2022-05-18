H,M=input().split()
cook=int(input())
H=int(H)
M=int(M)
nH=H+int((M+cook)/60)
nM=(M+cook)%60
if nH>23:
    nH=nH-24
print(nH, nM)
