n, m = [3, 5]

A = [1, 5, 3]
B = [3, 6, -7, 5, 4]

tmp = [[x*y for x, y in zip(A[:], B[i:i + n])] for i in range(m-n + 1)] if n < m else [[x*y for x, y in zip(A[i:i + n], B[:])] for i in range(n-m + 1)]

print(tmp)
print([sum(x) for x in tmp])
print(max([sum(x) for x in tmp]))

print(B[i:i +n] for i in range(m-n+1))
