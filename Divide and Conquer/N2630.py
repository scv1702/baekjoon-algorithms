import sys

white = 0
blue = 0

# 종이가 모두 같은 색으로 칠해져 있지 않으면, 가로와 세로로 중간 부분을 자른다.
# 이를 모두 같은 색으로 칠해져 있거나 하나의 정사각형 칸이 될 때까지 반복한다.

# start postion: (i, j)
def cut(matrix, i, j, n):
    if are_they_same_color(matrix, i, j, n):
        return 
    else:
        n = n // 2
        cut(matrix, i, j, n)
        cut(matrix, i, j + n, n)
        cut(matrix, i + n, j, n)
        cut(matrix, i + n, j + n, n)

def are_they_same_color(matrix, i, j, n):
    global white, blue

    color = matrix[i][j]

    for row in range(i, i + n):
        for col in range(j, j + n):
            if matrix[row][col] != color:
                return False
    
    if color == 0:
        white += 1
        return True
    else:
        blue += 1
        return True

N = int(sys.stdin.readline().rstrip())
paper = [0 for x in range(N)]

for i in range(N):
    paper[i] = list(map(int, sys.stdin.readline().rstrip().split()))

cut(paper, 0, 0, N)

print(white)
print(blue)