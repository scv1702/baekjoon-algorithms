import sys

N = int(sys.stdin.readline().rstrip())

for i in range(0, N, 1):
    print(' '*(i) + '*'*(2*(N-i)-1))

for j in range(1, N, 1):
    print(' '*(N-1-j) + '*'*(2*j+1))