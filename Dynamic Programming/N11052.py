import sys

'''
4
1 5 6 7

1
1+(1) / 5
1+(1+1) 1+(5) / 5+(1) / 6
1+(1+1+1) 1+(1+5) 1+(6) / 5+(1+1) 5+(5) / 7

1
2, 5 -> 5
6, 6 -> 6
7, 5+5, 6+1, 7 -> 10
'''

def solve(N, P):
    # 최대값을 저장
    dp_table = [0] * (N+1)

    # 카드를 1개 뽑는 경우
    dp_table[1] = P[1]

    # i: 뽑을 카드 개수
    for i in range(2, N+1):
        max_table = []

        for j in range(1, i+1):
            # 가장 먼저 P_j 카드팩을 뽑는 경우
            max_table.append(P[j] + dp_table[i-j])
        dp_table[i] = max(max_table)

    return dp_table[N]

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().rstrip().split()))
P.insert(0, 0)

print(solve(N, P))