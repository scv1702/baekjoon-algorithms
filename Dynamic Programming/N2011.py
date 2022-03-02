import sys

'''
25114

2
(2) 5, (2)5
(2 5) 1, (25) 1
(2 5 1) 1, (2 5 1)1, (25 1) 1, (25 1)1
(2 5 1 1) 4, (2 5 1 1)4, (2 5 11) 4, (25 1 1) 4, (25 1 1)4, (25 11) 4

'''
def solve(cypher):
    cypher.insert(0)

    N = len(cypher)

    dp_table = [0] * N
    
    dp_table[1] = 1
    
    for i in range(2, N+1):
       


cypher = list(sys.stdin.readline().rstrip())
cypher = list(map(int, cypher))

print(solve(cypher) % 1000000)
