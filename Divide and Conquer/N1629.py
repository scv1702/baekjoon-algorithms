import sys

# Tip: modulo opeartion도 distributive law가 성립한다.

def solve(A, B, C):
    # base case
    if B == 0:
        return 1
    else:
        # divide
        temp = solve(A, B//2, C)

        # conquer
        # if b is even
        if B % 2 == 0:
            return (temp * temp) % C
        # if b is odd
        else:
            return (temp * temp * (A % C)) % C

A, B, C = map(int, sys.stdin.readline().split())

print(solve(A, B, C))