import sys

input_str = list(sys.stdin.readline().rstrip())

for i in range(1, len(input_str) + 1, 1):
    print(input_str[i-1], end="")
    if i % 10 == 0:
        print("\n", end="")