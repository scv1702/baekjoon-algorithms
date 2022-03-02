import sys

# 1 = 1
# 2 = 1+1, 2
# 3 = 1+1+1, 1+2, 2+1, 3
# 4 = 1+..., 2+..., 3+...

def solve(n):
    if n <= 2:
        return n

    dp_table = [0] * (n+1)

    dp_table[1] = 1
    dp_table[2] = 2
    dp_table[3] = 4

    for i in range(4, n+1):
        num_of_cases = 0
        
        # n = 1 + ...
        num_of_cases += dp_table[i-1]

        # n = 2 + ...
        num_of_cases += dp_table[i-2]

        # n = 3 + ...
        num_of_cases += dp_table[i-3]

        dp_table[i] = num_of_cases

    return dp_table[n]

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(solve(n))