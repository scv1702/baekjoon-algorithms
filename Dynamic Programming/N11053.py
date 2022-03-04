import sys

def solve(sequence, n):
    lengths = []
    
    for i in range(0, n):
        sub_sequence = sequence[i:]
        
        



    
N = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))

print(solve(sequence, N))