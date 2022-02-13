import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
min = 1000001
max = -1000001
for i in range(N):
    temp = nums[i]
    if nums[i] > max:
        max = nums[i]
    if nums[i] < min:
        min = nums[i]
print(min, max)