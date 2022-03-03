import sys

'''
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
00, 01, 02, 03, ... 09, 11, 12, 13, ... 19, 23, ... 99
000, 001, 002, ..., 111, 112, 113, ..., 999
'''

def solve(n):
    dp_table = [0] * (n+1)

    # dp_table[1][i]: 1의 자리수가 i인 수의 개수
    dp_table[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    if n >= 2:
        for i in range(2, n+1):     
            end_by_0 = sum(dp_table[i-1][:1])
            end_by_1 = sum(dp_table[i-1][:2])
            end_by_2 = sum(dp_table[i-1][:3])
            end_by_3 = sum(dp_table[i-1][:4])
            end_by_4 = sum(dp_table[i-1][:5])
            end_by_5 = sum(dp_table[i-1][:6])
            end_by_6 = sum(dp_table[i-1][:7])
            end_by_7 = sum(dp_table[i-1][:8])
            end_by_8 = sum(dp_table[i-1][:9])
            end_by_9 = sum(dp_table[i-1][:10])

            dp_table[i] = [end_by_0, end_by_1, end_by_2, end_by_3, end_by_4, end_by_5, end_by_6, end_by_7, end_by_8, end_by_9]
    
    return sum(dp_table[n])

N = int(sys.stdin.readline().rstrip())

print(solve(N) % 10007)