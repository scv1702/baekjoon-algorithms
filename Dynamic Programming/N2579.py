import sys

# 답안 숙지 후 작성한 풀이. 나중에 다시 풀어볼 것

def solve(steps, n):
    dp_table = [0] * 300

    # 계단이 1개만 있는 경우
    dp_table[0] = steps[0]

    # 계단이 2개 있는 경우
    dp_table[1] = max(steps[0] + steps[1], steps[1])

    # 계단이 3개 있는 경우
    # 1. steps[1]을 밟은 경우, steps[0]을 밟으면 안된다.
    # 2. steps[1]을 밟지 않은 경우, steps[0]을 밟아도 된다.
    dp_table[2] = max(steps[1] + steps[2], steps[0] + steps[2])

    # 1. steps[i-1]을 밟은 경우, dp_table[i] = dp_table[i-3] + steps[i-1] + steps[i]
    # 2. steps[i-1]을 밟지 않은 경우, dp_table[i] = dp_table[i-2] + steps[i] 
    for i in range(3, n):
        dp_table[i] = max(dp_table[i-3] + steps[i-1] + steps[i], dp_table[i-2] + steps[i])
    
    return dp_table[n-1]

N = int(sys.stdin.readline().rstrip())

steps = [0] * 300
for i in range(N):
    steps[i] = (int(sys.stdin.readline().rstrip()))

print(solve(steps, N))