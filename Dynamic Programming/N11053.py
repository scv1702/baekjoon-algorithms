import sys

# LIS: Longest Increasing Subsequence
def solve(sequence, n):
    dp_table = [0] * n

    # LIS의 길이를 저장한다.
    dp_table[0] = 1

    # sequence에는 LIS에서 max num이 될 수가 무조건 하나 존재한다.
    # 그렇다면, sequence[i]가 LIS의 max num이 된다고 가정하자.
    # sequence[i]보다 작은 수들로 만들 수 있는 LIS의 길이에 +1 한 것이 현재 LIS의 길이이다.
    for i in range(1, n):
        # sequence[i]보다 작은 수가 없다면, LIS의 길이는 1
        dp_table[i] = 1
        for j in range(0, i):
            if sequence[j] < sequence[i]:
                dp_table[i] = max(dp_table[i], dp_table[j] + 1)

    return max(dp_table)

N = int(sys.stdin.readline().rstrip())

sequence = [0] * 1000

temp = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(len(temp)):
    sequence[i] = temp[i]

print(solve(sequence, N))