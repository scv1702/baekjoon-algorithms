import sys

def solve(sequence, n):
    dp_table = [0] * 1000

    dp_table[0] = 1
    max_term = sequence[0]

    # A = {10, 20, 10, 30, 20, 50}
    '''
    1 10
    2 20
    2 20
    3 30
    3 30
    4 50


    '''


    '''
    10
    10 20
    10 20
    10 20 30
    10 20 30
    10 20 30 50
    '''

    # A = {6, 7, 1, 2, 3, 4, 5}
    '''
    6
    6 7
    6 7
    6 7 / 1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    '''

    '''
    1 6
    2 7
    2 7
    2 7 / 2 2
    3 3
    4 4 
    5 5

    
    '''

    # 1. sequence[i]가 가장 긴 증가하는 부분 수열에 속하는 경우 -> sequence[i]가 가장 긴 증가하는 부분 수열의 최대항보다 큰 경우 
    # 2. sequence[i]가 가장 긴 증가하는 부분 수열에 속하지 않는 경우 -> sequence[i]가 가장 긴 증가하는 부분 수열의 최대항보다 크지 않은 경우

    for i in range(1, n):
        
        dp_table[i] = dp_table[i-1] + 1
        

        
    
N = int(sys.stdin.readline().rstrip())

sequence = [0] * 1000

temp = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(len(temp)):
    sequence[i] = temp[i]

print(solve(sequence, N))