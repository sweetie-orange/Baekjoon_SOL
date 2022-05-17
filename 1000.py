A,B=input().split()
#space로 분리된 글자가 들어왔을 때 split()을 이용해 쪼개서 저장.

print(int(A)+int(B))
#input으로 들어온 값은 str가 기본형이기 때문에 바꿔야함.
#그렇지 않을경우 1 2 > 12 형태로 나오게 됨.
