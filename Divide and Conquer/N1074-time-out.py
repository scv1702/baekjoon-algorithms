import sys

k = 0
flag = 0

# (r, c)를 몇 번째로 방문하지는지 출력
# i: start row, j: start col, n: length
def divide(i, j, n):
    global k
    global flag

    if n == 1:
        if i == r and j == c:
            flag = k
        else:
            k += 1
        return
    else:
        n = n // 2
        divide(i, j, n)
        divide(i, j + n, n)
        divide(i + n, j, n)
        divide(i + n, j + n, n)

N, r, c = map(int, sys.stdin.readline().rstrip().split())

divide(0, 0, 2 ** N)
print(flag)