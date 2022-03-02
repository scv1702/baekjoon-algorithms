import sys

# return: 1x2, 2x1 타일을 이용한 2xn 직사각형을 채우는 경우의 수
def solve(n):
    if n == 1:
        return 1
    
    dp_table = [0] * (n + 1)

    # 2x1일 때 경우의 수
    dp_table[1] = 1

    # 2x2일 때 경우의 수
    dp_table[2] = 2

    for i in range(3, n + 1):
        num_of_cases = 0

        # 2x1이 먼저 오는 경우
        num_of_cases += dp_table[i-1]

        # 1x2이 먼저 오는 경우
        num_of_cases += dp_table[i-2]

        dp_table[i] = num_of_cases

    return dp_table[n]
        
n = int(sys.stdin.readline().rstrip())

print(solve(n) % 10007)