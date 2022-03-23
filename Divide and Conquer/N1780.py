import sys

minus_one = 0
zero = 0
one = 0

def divide(matrix, i, j, n):
    if conquer(matrix, i, j, n):
        return
    else:
        n = n // 3
        divide(matrix, i, j, n)
        divide(matrix, i, j + n, n)
        divide(matrix, i, j + 2*n, n)

        divide(matrix, i + n, j, n)
        divide(matrix, i + n, j + n, n)
        divide(matrix, i + n, j + 2*n, n)

        divide(matrix, i + 2*n, j, n)
        divide(matrix, i + 2*n, j + n, n)
        divide(matrix, i + 2*n, j + 2*n, n)

def conquer(matrix, i, j, n):
    global minus_one
    global zero
    global one

    for row in range(i, i + n):
        for col in range(j, j + n):
            if matrix[i][j] != matrix[row][col]:
                return False

    if matrix[i][j] == -1:
        minus_one += 1
    elif matrix[i][j] == 0:
        zero += 1
    elif matrix[i][j] == 1:
        one += 1
    return True

n = int(sys.stdin.readline().rstrip())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
divide(matrix, 0, 0, n)

print(minus_one)
print(zero)
print(one)
