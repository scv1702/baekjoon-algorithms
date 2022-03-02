import sys
import math

'''
1 = 1^2
2 = 1^2 + 1^2
3 = 1^2 + 1^2 + 1^2

4 = 2^2
5 = 2^2 + 1^2
6 = 2^2 + 1^2 + 1^2
7 = 2^2 + 1^2 + 1^2 + 1^2
8 = 2^2 + 2^2

9 = 3^2
10 = 3^2 + 1^2
11 = 3^2 + 1^2 + 1^2
12 = 3^2 + 1^2 + 1^2 + 1^2
13 = 3^2 + 2^2
14 = 3^2 + 2^2 + 1^2
15 = 3^2 + 2^2 + 1^2 + 1^2

16 = 4^2
52 = 7^2 + 1^2 + 1^2 + 1^2
6^2 + 4^2
'''

def solve(N):
    dp_table = [0] * (N+1)

    if N <= 3:
        return N

    dp_table[1] = 1
    dp_table[2] = 2
    dp_table[3] = 3

    for i in range(4, N+1):
        dp_table[i] = 1 + dp_table[int(i - math.pow(int(math.sqrt(i)), 2))]

    return dp_table[N]

N = int(sys.stdin.readline().rstrip())

print(solve(N))