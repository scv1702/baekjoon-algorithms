import sys
import math

def solve(n):
    dp_table = [0] * 100001

    dp_table[1] = 1
    dp_table[2] = 2
    dp_table[3] = 3

    for i in range(4, n+1):
        terms = []
        for j in range(1, int(math.sqrt(i)) + 1):
            terms.append(1 + dp_table[i - j ** 2])
        dp_table[i] = min(terms)

    return dp_table[n]

N = int(sys.stdin.readline().rstrip())

print(solve(N))