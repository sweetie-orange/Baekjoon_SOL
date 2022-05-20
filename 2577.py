A=int(input())
B=int(input())
C=int(input())
X=A*B*C
L=[0,0,0,0,0,0,0,0,0,0]
while(X>0):
    na=X%10
    X=int(X/10)
    L[na]=L[na]+1
for x in L:
    print(x)
