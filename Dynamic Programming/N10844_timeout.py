import sys

'''
경계값, 끝이 0으로 끝나거나 9로 끝나면 다음 숫자는 1개만

(101, 210)
N=1: (1) (2) (3) ... (9)
N=2: (10, 12) (21, 23) (32, 34) ... (76, 78) (87, 89) (98)
! N=3: (101) (121, 123) (210, 212) (232, 234) ... (765, 767) (787, 789) (876, 878) (898) (987, 989)
N=4: (1010, 1012) (1210, 1212) (1232, 1234) ... (2101) (2121, 2123) ... (8765, 8767) (8787, 8789) (8987, 8989)
! N=5: (10101) (10121, 10123) (12101) (12121, 12123) ... 
'''

def solve(n):
    dp_table = [0] * (n+1)

    # n = 1
    dp_table[1] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if n >= 2:
        for i in range(2, n+1):
            dp_table[i] = []
            for j in range(0, len(dp_table[i-1])):
                temp = dp_table[i-1][j]
                for k in range(0, 10):
                    if abs(temp % 10 - k) == 1:
                        dp_table[i].append(temp * 10 + k)
            print(dp_table[i])
    return len(dp_table[n])

# 1 <= N <= 100
N = int(sys.stdin.readline().rstrip())

print(solve(N) % (10 ** 9))
