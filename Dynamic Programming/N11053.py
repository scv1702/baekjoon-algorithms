import sys

# A = {10, 20, 10, 30, 20, 50}
# A = {10, 50, 10, 20, 30, 20}
# A = {50, 10, 60, 20, 40, 30}

'''
n=1, 10
n=2, 10 20
n=3, 10 20 30
n=4, 10 20 30 50
n=5, 

'''
def solve(sequence):
    indexs = []

    
N = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))

print(solve(sequence))