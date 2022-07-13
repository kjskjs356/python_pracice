import sys

sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    print("#{}".format(i+1))
    ans = ""
    for _ in range(N):
        Ci, Ki = sys.stdin.readline().split()
        Ki = int(Ki)
        ans += Ci*Ki

    for i in range(len(ans)):
        if (i+1) % 10 != 0:
            print(ans[i], end="")
        else:
            print(ans[i])
    print()
