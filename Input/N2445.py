import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N+1, 1):
    # 총 길이: 2*N
    print('*'*(i) + ' '*(2*(N-i)) + '*'*(i))

for i in range(N-1, 0, -1):
    # 총 길이: 2*N
    print('*'*(i) + ' '*(2*(N-i)) + '*'*(i))