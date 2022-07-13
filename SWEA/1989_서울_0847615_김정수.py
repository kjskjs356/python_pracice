#초심자의 회문 검사
N = int(input())
word = []

for i in range(N):
    word.append(input())

for i in range(N):
    if list(word[i]) == list(''.join(reversed(word[i]))):
        print("#{}".format(i+1), "1")
    else:
        print("#{}".format(i+1), "0")
