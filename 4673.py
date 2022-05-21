L=list(range(1,10000))
M=list(range(1,10000))
def d(x):
    if x<10:
        ans=x+x
    elif x<100:
        ans=x+int(x/10)+x%10
    elif x<1000:
        ans=x+int(x/100)+int(x%100/10)+x%10
    else:
        ans=x+int(x/1000)+int(x%1000/100)+int(x%100/10)+x%10
    if ans in M:
        M.remove(ans)

for x in L:
    d(x)

for i in M:
    print(i)
