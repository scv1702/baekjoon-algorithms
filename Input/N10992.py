import sys

N = int(sys.stdin.readline().rstrip())
if N != 1:
    print(' '*(N-1) + '*')
    for i in range(2, N):
        print(' '*(N-i) + '*' + ' '*(2*i-3) + '*')
    print('*'*(2*N-1))
else:
    print('*')