import sys

N = int(sys.stdin.readline())
nums = list(sys.stdin.readline().rstrip())
nums = map(int, nums)
print(sum(nums))