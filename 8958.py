Test=int(input())
for i in range(0,Test):
    result=list(input())
    G=0
    point=0
    for i in result:
        if i=="O":
            point=point+1+G
            G=G+1
        else:
            G=0
    print(point)
