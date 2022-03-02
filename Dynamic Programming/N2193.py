import sys

# n=1, !1
# n=2, 10
# n=3, 100, !101
# n=4, 1000, !1001, 1010
# n=5, 10000, !10001, 10010, 10100, !10101
# n=6, 100000, !100001, 100010, 100100, 100101, 101000, !101001, 101010

def solve(n):
    dp_table = [(0, 0)] * (n+1)

    # (끝이 0인 수 개수, 끝이 1인 수 개수)
    dp_table[1] = (0, 1)

    # 끝이 0이면, 다음에 0 또는 1
    # 끝이 1이면, 다음에 무조건 0
    for i in range(2, n+1):
        num_of_zero = dp_table[i-1][0] + dp_table[i-1][1] 

        num_of_one = dp_table[i-1][0]

        dp_table[i] = (num_of_zero, num_of_one)
    
    return dp_table[n][0] + dp_table[n][1]

N = int(sys.stdin.readline().rstrip())

print(solve(N))