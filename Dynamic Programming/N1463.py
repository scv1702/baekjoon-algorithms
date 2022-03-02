import sys

# 1 <= N <= 10^6
N = int(sys.stdin.readline().rstrip())

# 점화식을 생각해보자.
# 1: 0
# 2 -> 1: 1
# 3 -> 1: 1
# 4 -> (2 -> 1): 2
# 5 -> (4 -> 2 -> 1): 3
# 6 -> (2 -> 1): 2
# 7 -> (6 -> 2 -> 1): 3
# 8 -> (4 -> 2 -> 1): 3
# 9 -> (3 -> 1): 2
# 10 -> (9 -> 3 -> 1): 3

count_table = [0] * int(10 ** 6)

# X = 1
count_table[0] = 0

# X = 2 ~ X = N
for i in range(1, N):
    temp = i + 1
    counts = []

    # 3의 배수인 경우
    if int(temp % 3) == 0:
        X = int(temp / 3)
        counts.append(1 + count_table[X-1])
    
    # 2의 배수인 경우
    if int(temp % 2) == 0:
        X = int(temp / 2)
        counts.append(1 + count_table[X-1])

    X = temp - 1
    counts.append(1 + count_table[X-1])

    count_table[i] = min(counts)

print(count_table[N-1])