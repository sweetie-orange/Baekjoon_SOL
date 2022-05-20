N=int(input())
if 0>N or N>99:
    end


if N<10:
    J=N
else:
    J=(int(N/10)+N%10)%10
F=(N%10)*10+J

n=1

while(N!=F):
    if F<10:
        J=F
        n=n+1
    else:
        J=(int(F/10)+F%10)%10
        n=n+1
    F=(F%10)*10+J

print(n)
