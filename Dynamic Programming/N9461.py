import sys

# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
def P(N):
    dp_table = [0] * (N+1)

    if N <= 3:
        return 1

    dp_table[1] = 1
    dp_table[2] = 1
    dp_table[3] = 1

    for i in range(4, N+1):
        dp_table[i] = dp_table[i-2] + dp_table[i-3]

    return dp_table[N]

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(P(N))