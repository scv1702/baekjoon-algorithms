import sys

'''
끝이 0으로 끝나거나 9로 끝나면 다음 반복에 계단수 1개만 생성. 그렇지 않으면 2개 생성

N=1: (1) (2) (3) ... (9) 
N=2: (10, 12) (21, 23) (32, 34) ... (76, 78) (87, 89) (98)
N=3: (101) (121, 123) (210, 212) (232, 234) ... (765, 767) (787, 789) (876, 878) (898) (987, 989) 
N=4: (1010, 1012) (1210, 1212) (1232, 1234) (2101) (2121, 2123) ... (8765, 8767) (8787, 8789) (8987, 8989) (9876, 9878) (9898) 
N=5: (10101) (10121, 10123) (12101) (12121, 12123) ...
N=6: (101010, 101012) (101210, 101212) (101232, 101234) ... 
'''

def solve(n):
    dp_table = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * (n+1)

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