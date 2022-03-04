import sys

def solve(stickers, N):


T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    stickers = [0] * 2
    for j in range(2):
        stickers[j] = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solve(stickers, N))