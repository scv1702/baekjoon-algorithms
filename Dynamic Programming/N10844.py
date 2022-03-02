import sys

def solve(n):
    dp_table = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * (n+1)

    # dp_table[1][i]: 1의 자리수가 i인 수의 개수
    dp_table[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    if n >= 2:
        for i in range(2, n+1): 
            end_by_0 = dp_table[i-1][1]
            end_by_1 = dp_table[i-1][0] + dp_table[i-1][2]
            end_by_2 = dp_table[i-1][1] + dp_table[i-1][3]
            end_by_3 = dp_table[i-1][2] + dp_table[i-1][4]
            end_by_4 = dp_table[i-1][3] + dp_table[i-1][5]
            end_by_5 = dp_table[i-1][4] + dp_table[i-1][6]
            end_by_6 = dp_table[i-1][5] + dp_table[i-1][7]
            end_by_7 = dp_table[i-1][6] + dp_table[i-1][8]
            end_by_8 = dp_table[i-1][7] + dp_table[i-1][9]
            end_by_9 = dp_table[i-1][8]
            
            dp_table[i] = [end_by_0, end_by_1, end_by_2, end_by_3, end_by_4, end_by_5, end_by_6, end_by_7, end_by_8, end_by_9]
    
    return sum(dp_table[n])

# 1 <= N <= 100
N = int(sys.stdin.readline().rstrip())

print(solve(N) % (10 ** 9))