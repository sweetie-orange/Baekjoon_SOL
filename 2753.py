ye=int(input())
if ye%4==0:
    if ye%400==0:
        print("1")
    elif ye%100==0:
        print("0")
    else:
        print("1")
else:
    print("0")
