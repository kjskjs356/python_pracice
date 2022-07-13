#1대1 가위바위보
A, B = map(int, input().split())

if A - B == 1 or A - B == -2 :
    print("A")
else:
    print("B")