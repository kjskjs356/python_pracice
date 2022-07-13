import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
print(num[((N-1)//2)])