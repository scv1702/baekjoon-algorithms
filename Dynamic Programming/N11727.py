import sys

'''
n=1: (2x1)
n=2: (2x1, 2x1) (1x2, 1x2) (2x2)
n=3: (1x2, 1x2, n=1) (2x1, n=2) (2x2, 2x1, n=1)
n=4: (1x2, 1x2, n=2) (2x1, n=3) (2x2, n=2)
'''

def solve(n):
    if n == 1:
        return 1

    dp_table = [0] * (n+1)

    # n = 1 
    dp_table[1] = 1

    # n = 2
    dp_table[2] = 3

    for i in range(3, n+1):
        num_of_cases = 0

        # 1x2이 먼저 오는 경우
        num_of_cases += dp_table[i-2]

        # 2x1이 먼저 오는 경우
        num_of_cases += dp_table[i-1]

        # 2x2이 먼저 오는 경우
        num_of_cases += dp_table[i-2]

        dp_table[i] = num_of_cases

    return dp_table[n]

n = int(sys.stdin.readline().rstrip())

print(solve(n) % 10007)