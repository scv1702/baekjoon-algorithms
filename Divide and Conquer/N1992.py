import sys

def divide(matrix, i, j, n):
    quad_tree = []
    bit = conquer(matrix, i, j, n)
    if bit != -1:
        quad_tree.append(bit)
        return quad_tree
    else:
        n = n // 2
        quad_tree += ['('] + divide(matrix, i, j, n)
        quad_tree += divide(matrix, i, j + n, n)
        quad_tree += divide(matrix, i + n, j, n)
        quad_tree += divide(matrix, i + n, j + n, n) + [')']
        return quad_tree

def conquer(matrix, i, j, n):
    bit = matrix[i][j]
    for row in range(i, i + n):
        for col in range(j, j + n):
            if bit != matrix[row][col]:
                return -1
    return bit

n = int(sys.stdin.readline().rstrip())
video = [0] * n
for i in range(n):
    video[i] = list(map(int, list(sys.stdin.readline().rstrip())))
quad_tree = divide(video, 0, 0, n)
for i in range(len(quad_tree)):
    print(quad_tree[i], end='')